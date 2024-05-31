import click
import sys


def create_session(session_name=None, user_name=None):
    print("Placeholder create-session function")


def join_session(session_name=None, user_name=None):
    print("Placeholder join-session function")


@click.command()
@click.argument("command", required=1)
@click.option(
    "--session-name", help="Custom session name to join or create", default=None
)
@click.option(
    "--user-name", help="Custom username to be used in an active session", default=None
)
def main(command, session_name=None, user_name=None):
    """
    Main module for msglite program.
    """
    fn_dict = {"create-session": "create_session", "join-session": "join_session"}
    exec(f"{fn_dict[command]}()")
