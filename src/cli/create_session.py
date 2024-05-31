#!/usr/bin/env python3


def create_session(args: dict = None):
    """
    Create a new session via the create-session command.
    This function spins up a kafka topic and subscribes to messages from this
    topic. It generates a session ID string and returns this value to the user
    to share with invitees.
    """
    print("In the create_session function")
    print(args)
