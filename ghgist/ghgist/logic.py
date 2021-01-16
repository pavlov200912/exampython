'''Main logic of application.'''

import json
from typing import Dict, Final, List, Tuple

import requests

GITHUB_API: Final = 'https://api.github.com'
REQUEST_PARAMS: Final = {'scope': 'gist'}


def _construct_token_header(token: str) -> Dict[str, str]:
    return {'Authorization': 'token {0}'.format(token)}


def list_gists(token: str) -> List[Tuple[str, str, str]]:
    """List all gists of auth user.

    :param token: user token
    """
    url = '{0}/gists'.format(GITHUB_API)

    payload: Dict[str, str] = {}

    github_response = requests.get(
        url,
        headers=_construct_token_header(token),
        params=REQUEST_PARAMS,
        data=json.dumps(payload),
    )

    github_response.raise_for_status()

    parsed_response = github_response.json()
    gist_list = []
    for gist_info in parsed_response:
        id = gist_info['id']
        filename = list(gist_info['files'].values())[0]['filename']
        url = gist_info['html_url']
        gist_list.append((id, filename, url))

    return gist_list


def create(token: str, filename: str) -> None:
    url = '{0}/gists'.format(GITHUB_API)

    with open(filename, 'r') as content_file:
        content = content_file.read()

    payload = {'description': 'GIST created by ghgist',
               'public': True,
               'files': {
                   filename: {'content': content}
               }
               }

    github_response = requests.post(
        url,
        headers=_construct_token_header(token),
        params=REQUEST_PARAMS,
        data=json.dumps(payload),
    )

    github_response.raise_for_status()


def update(token: str, gist_id: str, filename: str) -> None:
    url = '{0}/gists/{1}'.format(GITHUB_API, gist_id)

    with open(filename, 'r') as content_file:
        content = content_file.read()

    payload = {'description': 'GIST created by ghgist',
               'gist_id': gist_id,
               'files': {
                   filename: {'content': content}
               }
               }

    github_response = requests.patch(
        url,
        headers=_construct_token_header(token),
        params=REQUEST_PARAMS,
        data=json.dumps(payload),
    )

    github_response.raise_for_status()


def download(token: str, gist_id: str, dest_path: str) -> None:
    url = '{0}/gists/{1}'.format(GITHUB_API, gist_id)

    payload = {'gist_id': gist_id}

    github_response = requests.get(
        url,
        headers=_construct_token_header(token),
        params=REQUEST_PARAMS,
        data=json.dumps(payload),
    )

    github_response.raise_for_status()

    parsed_response = github_response.json()
    gist_files = parsed_response['files']
    gist_content = list(gist_files.values())[0]['content']

    with open(dest_path, 'w') as file_from_gist:
        file_from_gist.write(gist_content)


def delete(token: str, gist_id: str) -> None:
    url = '{0}/gists/{1}'.format(GITHUB_API, gist_id)

    payload = {'gist_id': gist_id}

    github_response = requests.delete(
        url,
        headers=_construct_token_header(token),
        params=REQUEST_PARAMS,
        data=json.dumps(payload),
    )

    github_response.raise_for_status()
