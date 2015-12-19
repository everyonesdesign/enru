#!/usr/bin/env python
import sys
import subprocess

from src.enru import Enru
from src.parsers.yandex import YandexParser

word = sys.argv[1]

parser = YandexParser()
enru = Enru(parser)
content = enru.run(word)

content