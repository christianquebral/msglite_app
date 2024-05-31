#!/usr/bin/env python3


def join_session(args: dict = None):
    """
    Join a session via the join-session command.
    This function attempts to subscribe to an existing Kafka topic and returns
    new messages from that topic.
    """
    print("In the join-session function")
    print(args)
