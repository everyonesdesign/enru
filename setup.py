#!/usr/bin/env python

from distutils.core import setup

setup(
    name='enru',
    version='1.0',
    description='Yandex.Dictionary translation parser',
    author='Yura Trambitskiy',
    author_email='tr.yura@yahoo.com',
    url='https://github.com/everyonesdesign/enru-python/',
    py_modules=['enru'],
    requires=[
        'beautifulsoup4==4.4.1',
        'termcolor==1.1.0',
    ],
)