import json
from typing import Final, Dict, Any, Tuple, List

import requests

GITHUB_API: Final = "https://api.github.com"


def list_gists(token: str) -> List[Tuple[str, str, str]]:
    url = GITHUB_API + "/gists"

    headers = {'Authorization': 'token %s' % token}
    params = {'scope': 'gist'}
    payload = {}

    res = requests.get(url, headers=headers, params=params,
                       data=json.dumps(payload))
    res.raise_for_status()

    parsed_response = res.json()
    gist_list = []
    for gist_info in parsed_response:
        id = gist_info['id']
        filename = list(gist_info['files'].values())[0]['filename']
        url = gist_info['html_url']
        gist_list.append((id, filename, url))

    return gist_list


def create(token: str, filename: str) -> None:
    url = GITHUB_API + "/gists"

    with open(filename, 'r') as content_file:
        content = content_file.read()

    headers = {'Authorization': 'token %s' % token}
    params = {'scope': 'gist'}
    payload = {"description": "GIST created by ghgist",
               "public": True,
               "files": {
                   filename: {"content": content}
               }
               }

    res = requests.post(url, headers=headers, params=params,
                        data=json.dumps(payload))

    res.raise_for_status()


def update(token: str, gist_id: str, filename: str):
    url = GITHUB_API + "/gists/" + gist_id

    with open(filename, 'r') as content_file:
        content = content_file.read()

    headers = {'Authorization': 'token %s' % token}
    params = {'scope': 'gist'}
    payload = {"description": "GIST created by ghgist",
               "gist_id": gist_id,
               "files": {
                   filename: {"content": content}
               }
               }

    res = requests.patch(url, headers=headers, params=params,
                         data=json.dumps(payload))

    res.raise_for_status()


def download(token: str, gist_id: str, dest_path: str) -> None:
    url = GITHUB_API + "/gists/" + gist_id

    headers = {'Authorization': 'token %s' % token}
    params = {'scope': 'gist'}
    payload = {"gist_id": gist_id}

    res = requests.get(url, headers=headers, params=params,
                       data=json.dumps(payload))

    res.raise_for_status()

    parsed_response = res.json()
    gist_files = parsed_response['files']
    gist_content = list(gist_files.values())[0]['content']

    with open(dest_path, 'w') as file_from_gist:
        file_from_gist.write(gist_content)


def delete(token: str, gist_id: str):
    url = GITHUB_API + "/gists/" + gist_id

    headers = {'Authorization': 'token %s' % token}
    params = {'scope': 'gist'}
    payload = {"gist_id": gist_id}

    res = requests.delete(url, headers=headers, params=params,
                          data=json.dumps(payload))

    res.raise_for_status()
