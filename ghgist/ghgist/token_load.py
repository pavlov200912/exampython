"""Loading setting from .ghist file."""
import json


class InvalidTokenException(Exception):
    """Exception for invalid token read."""


def load(path: str = '.ghgist') -> str:
    """
    Read token from configure file.

    :param path: path to token, .ghgist by default
    :return: token
    """
    with open(path, 'r') as config_file:
        config = json.loads(config_file.read())

        try:
            auth_settings = config['ghgist']['settings']
        except ValueError:
            raise InvalidTokenException("File doesn't have settings inside")

        try:
            token = auth_settings['token']
        except ValueError:
            raise InvalidTokenException("Setting doesn't have token property")
    return token
