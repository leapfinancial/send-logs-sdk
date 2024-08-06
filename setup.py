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
    author='Ruben Gonzalez',
    author_email='ruben@leapfinancial.com',
    description='Esta libreria envia los logs a pub sub',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tuusuario/sendlogssdk',  # URL del repositorio del proyecto
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)