import argparse
import sys


def create_session():
    print("Placeholder create-session function")


def main():
    """
    Main module for msglite program.
    """
    fn_dict = {
        "create-session": "create_session"
    }

    parser = argparse.ArgumentParser(
        description="A CLI-based private text messaging program"
    )

    # TBD this is a temporary solution until I figure out better ways for
    # executing python functions via arguments.
    parser.add_argument("cmd", type=str, help="create")

    arg = parser.parse_args().arg
    
    exec(f"{fn_dict[arg.arg]}()")
