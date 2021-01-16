import sys
from typing import List
from ghgist import token_load
from ghgist import logic


def run() -> None:
    arguments = sys.argv[1:]

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
        token = token_load.load()
    except token_load.InvalidTokenException as e:
        print(e)
    return token


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
        return
    token = load_token_safe()
    gist_list = logic.list_gists(token)
    for gist_info in gist_list:
        print(f"{gist_info[0]} {gist_info[1]}:{gist_info[2]}")


def create_command(arguments: List[str]) -> None:
    if len(arguments) != 2:
        print("Required 1 argument for create command")
        return
    token = load_token_safe()
    logic.create(token, filename=arguments[1])


def update_command(arguments: List[str]) -> None:
    if len(arguments) != 3:
        print("Required 2 argument for update command")
        return
    token = load_token_safe()
    logic.update(token, gist_id=arguments[1], filename=arguments[2])


def download_command(arguments: List[str]) -> None:
    if len(arguments) != 3:
        print("Required 2 argument for download command")
        return
    token = load_token_safe()
    logic.download(token, gist_id=arguments[1], dest_path=arguments[2])


def delete_command(arguments: List[str]) -> None:
    if len(arguments) != 2:
        print("Required 1 argument for create command")
        return
    token = load_token_safe()
    logic.delete(token, gist_id=arguments[1])


if __name__ == "__main__":
    run()
