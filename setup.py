from setuptools import setup

setup(
    name='django-command-disable',
    version='2021.6.17',
    install_requires=[
        'call'
    ],
    packages=[
        'django_command_disable',
        'django_command_disable.management',
        'django_command_disable.migrations'
    ]
)
