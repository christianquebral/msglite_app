#!/usr/bin/env python3

from kafka import KafkaConsumer, KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError


def create_session(args: dict = None):
    """
    Create a new session via the create-session command.
    This function spins up a kafka topic and subscribes to messages from this
    topic. It generates a session ID string and returns this value to the user
    to share with invitees.
    """
    print("In the create_session function")
    print(args)
    admin_client = KafkaAdminClient(
        bootstrap_servers="localhost:9092", client_id="test"
    )

    try:
        topics = [NewTopic(name="test_topic", num_partitions=1, replication_factor=1)]
        admin_client.create_topics(topics)
    except TopicAlreadyExistsError as e:
        # print(repr(e))
        pass

    producer = KafkaProducer(bootstrap_servers="localhost:9092")
    consumer = KafkaConsumer(
        "test_topic", bootstrap_servers="localhost:9092", auto_offset_reset="earliest"
    )
    producer.send("test_topic", b"Test Message")
    print("Sent message")
    for message in consumer:
        print(message.value.decode("utf-8"))
