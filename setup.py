from setuptools import setup, find_packages

setup(
    name='sendlogssdk',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'google-cloud-pubsub',
        'colorlog',
        'pydantic',
    ],
)