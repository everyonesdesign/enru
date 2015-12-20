#!/usr/bin/env python
import sys

from src.enru import Enru
from src.parsers.yandex import YandexParser


def main():
    word = sys.argv[1]
    parser = YandexParser()
    enru = Enru(parser)
    content = enru.run(word)
    content


if __name__ == "__main__":
    main()