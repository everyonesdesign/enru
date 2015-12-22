#!/usr/bin/env python
import click

from src.enru import Enru
from src.parsers.yandex import YandexParser


@click.command()
@click.argument('word')
@click.option('--show-examples', '-e', 
              is_flag=True,
              default=False, 
              help='Show word usage examples')
def main(word, show_examples):
    """Simple dictionaries translation parser"""
    parser = YandexParser()
    enru = Enru(parser)
    content = enru.run(word, show_examples)
    print(content)

if __name__ == "__main__":
    main()
