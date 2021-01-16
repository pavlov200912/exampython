import json
from typing import Final, Dict, Any, Tuple, List

import requests

GITHUB_API: Final = "https://api.github.com"


def api_call(url, http_method: str, token: str, payload=None):
    if payload is None:
        payload = {}
    headers = {'Authorization': f'token {token}'}
    params = {'scope': 'gist'}

    http_methods = {
        'get': requests.get,
        'post': requests.post,
        'patch': requests.patch,
        'delete': requests.delete
    }

    method = http_methods[http_method]
    res = method(url, headers=headers, params=params,
                 data=json.dumps(payload))
    res.raise_for_status()
    return res.json()


def list_gists(token: str) -> List[Tuple[str, str, str]]:
    url = GITHUB_API + "/gists"

    parsed_response = api_call(url, 'get', token)

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

    payload = {"description": "GIST created by ghgist",
               "public": True,
               "files": {
                   filename: {"content": content}
               }
               }

    api_call(url, 'post', token, payload)


def update(token: str, gist_id: str, filename: str):
    url = GITHUB_API + "/gists/" + gist_id

    with open(filename, 'r') as content_file:
        content = content_file.read()

    payload = {"description": "GIST created by ghgist",
               "gist_id": gist_id,
               "files": {
                   filename: {"content": content}
               }
               }

    api_call(url, 'patch', token, payload)


def download(token: str, gist_id: str, dest_path: str) -> None:
    url = GITHUB_API + "/gists/" + gist_id
    payload = {"gist_id": gist_id}

    parsed_response = api_call(url, 'get', token, payload)

    gist_files = parsed_response['files']
    gist_content = list(gist_files.values())[0]['content']

    with open(dest_path, 'w') as file_from_gist:
        file_from_gist.write(gist_content)


def delete(token: str, gist_id: str):
    url = GITHUB_API + "/gists/" + gist_id
    payload = {"gist_id": gist_id}

    api_call(url, 'delete', token, payload)
