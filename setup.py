#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='enru',
    version='1.0',
    description='Yandex.Dictionary translation parser',
    author='Yura Trambitskiy',
    author_email='tr.yura@yahoo.com',
    license='MIT',
    url='https://github.com/everyonesdesign/enru-python/',
    entry_points={
        'console_scripts': [
            'enru = init',
        ],
    },
    install_requires=[
        'lxml',
        'beautifulsoup4==4.4.1',
        'termcolor==1.1.0',
    ],
)
