from ghgist import __version__
from ghgist import logic
from ghgist import token_load
import json

def test_version():
    assert __version__ == "0.1.0"


def test_api_call():
    token: dict = {
        "ghgist": {"settings": {"token": "test "}}
    }
    with open('.test', 'w') as f:
        f.write(json.dumps(token))

    token = token_load.load('.test')
    assert 'test' in token
