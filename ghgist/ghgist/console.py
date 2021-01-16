import sys
from typing import List
import token_load
import logic

def run() -> None:
    arguments = sys.argv[1:]

    print(sys.argv, arguments)

    if len(arguments) == 0:
        help_command(arguments=[])
        return

    commands_dict = {
        '--help': help_command,
        'list': list_command,
        'create': create_command,
        'update': update_command,
        'download': download_command,
        'delete': delete_command,
    }

    command = arguments[0]
    if command in commands_dict:
        commands_dict[command](arguments)
    else:
        print(f"Can't perform {command} command. Please read help:")
        help_command(arguments=[])


def load_token_safe() -> str:
    try:
        return token_load.load()
    except token_load.InvalidTokenException as e:
        print(e)


def help_command(arguments) -> None:
    print("""
    Commands:
    --help - show command usage
    
    list - list all gists for auth user
    
    create <filename> - create new gist from local file
    
    update <gist_id> <filename> - update gist by gist_id with content from file
    
    download <gist_id> <destination_path> - download last gist content by id
    
    delete <gist_id> - delete gist by id
    """)  # TODO: help message


def list_command(arguments: List[str]) -> None:
    if len(arguments) > 1:
        print("Too many arguments for list command")
    token = load_token_safe()


def create_command(arguments: List[str]) -> None:
    ...


def update_command(arguments: List[str]) -> None:
    ...


def download_command(arguments: List[str]) -> None:
    ...


def delete_command(arguments: List[str]) -> None:
    ...


if __name__ == "__main__":
    run()
