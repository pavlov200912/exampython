import sys
from typing import List

from ghgist import logic, token_load


def run() -> None:
    """Main function that run CLI logic."""
    arguments = sys.argv[1:]

    if not arguments:
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
    command_handler = commands_dict.get(command)
    if command_handler is not None:
        command_handler(arguments)
    else:
        print("Can't perform {0} command. Please read help:".format(command))
        help_command(arguments=[])


def help_command() -> None:
    """Show help."""
    print("""  
    Commands:
    --help - show command usage
    list - list all gists for auth user
    create <filename> - create new gist from local file
    update <gist_id> <filename> - update gist by gist_id with content from file
    download <gist_id> <destination_path> - download last gist content by id
    delete <gist_id> - delete gist by id""".strip(),
          )


def list_command(arguments: List[str]) -> None:
    """
    Run logic function list and print the result.

    :param arguments: 'list'
    """
    if len(arguments) > 1:
        print('Too many arguments for list command')  # noqa: WPS421
        return
    token = token_load.load()
    gist_list = logic.list_gists(token)
    for gist_info in gist_list:
        print('{0} {1}:{2}'.format(*gist_info))


def create_command(arguments: List[str]) -> None:
    """
    Run logic function create and parse arguments.

    :param arguments: ['create', filename]
    """
    if len(arguments) != 2:
        print('Required 1 argument for create command')  # noqa: WPS421
        return
    token = token_load.load()
    logic.create(token, filename=arguments[1])


def update_command(arguments: List[str]) -> None:
    """
    Run logic function update and parse arguments.

    :param arguments: ['update', gist_id, filename]
    """
    if len(arguments) != 3:
        print('Required 2 argument for update command')  # noqa: WPS421
        return
    token = token_load.load()
    logic.update(token, gist_id=arguments[1], filename=arguments[2])


def download_command(arguments: List[str]) -> None:
    """
    Call logic download and pars args.

    :param arguments: 'download', gist_id and dest_path
    """
    if len(arguments) != 3:
        print('Required 2 argument for download command')  # noqa: WPS421
        return
    token = token_load.load()
    logic.download(token, gist_id=arguments[1], dest_path=arguments[2])


def delete_command(arguments: List[str]) -> None:
    """
    Call logic deletion and pars args.

    :param arguments: gist_id
    """
    if len(arguments) != 2:
        print('Required 1 argument for create command')  # noqa: WPS421
        return
    token = token_load.load()
    logic.delete(token, gist_id=arguments[1])


if __name__ == '__main__':
    run()
