from setuptools import setup, find_packages

setup(
    name='send-logs-sdk',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'google-cloud-pubsub',
        'colorlog',
        'pydantic',
    ],
)