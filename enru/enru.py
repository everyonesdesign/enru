import urllib

from bs4 import BeautifulSoup


class Enru:
    def __init__(self, parser):
        self.parser = parser

    def run(self, word, show_examples):
        url = self.get_url(word)
        markup = self.fetch(url)

        try:
            content = self.parse(markup, show_examples)
        except NothingFoundException:
            # TODO: add name of dictionary here
            content = "Слово «{word}» не найдено".format(word=word)

        return content

    def fetch(self, url):
        return urllib.urlopen(url)

    def parse(self, markup, show_examples):
        soup = BeautifulSoup(markup, "lxml")
        return self.parser.get_content(soup, show_examples)

    def get_url(self, word):
        return self.parser.get_url(word)


class NothingFoundException(Exception):
    pass
