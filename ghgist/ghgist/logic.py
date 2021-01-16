import json
from typing import Final

import requests

GITHUB_API: Final = "https://api.github.com"


def list_gists(token: str):
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


def create(token: str, filename: str):
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


def update(token: str, gist_id: str, filename: str):
    ...


def download(token: str, gist_id: str, dest_path: str):
    ...


def delete(token: str, gist_id: str):
    ...
