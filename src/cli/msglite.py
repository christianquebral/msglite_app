#!/usr/bin/env python3

from .create_session import create_session
from .join_session import join_session
import click
import sys


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
    Main entrypoint function to be called from msglite CLI.
    """
    fn_dict = {"create-session": "create_session", "join-session": "join_session"}
    exec(f"{fn_dict[command]}({session_name}, {user_name})")
