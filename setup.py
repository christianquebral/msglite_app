from setuptools import setup
from setuptools import find_packages

setup(
    name="msglite",
    description="msglite CLI program",
    long_description="CLI messaging program powered by Apache Kafka",
    version="1.0.0",
    url="https://github.com/christianquebral/msglite_app",
    author="Christian Quebral",
    author_email="christianquebral.dev@gmail.com",
    scripts=["app/msglite"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        "click==8.1.7",
        "kafka-python==2.0.2"
    ],
)
