#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='enru',
    version='1.1',
    description='Simple dictionaries translation parser',
    author='Yura Trambitskiy',
    author_email='tr.yura@yahoo.com',
    license='MIT',
    url='https://github.com/everyonesdesign/enru/',
    scripts=['bin/enru'],
    py_modules=['init'],
    packages=find_packages(),
    install_requires=[
        'lxml',
        'Click',
        'beautifulsoup4==4.4.1',
        'termcolor==1.1.0',
    ],
)
