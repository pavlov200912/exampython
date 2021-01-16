import json


class InvalidTokenException(Exception):
    ...


def load(path: str = '.ghgist'):
    with open(path, 'r') as config_file:
        try:
            config = json.loads(config_file.read())
            auth_settings = config['ghgist']['settings']
            token = auth_settings['token']
        except ValueError:
            raise InvalidTokenException(f"Can't get token from {path}")
            
    return token
