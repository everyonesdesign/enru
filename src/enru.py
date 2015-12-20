import urllib

from bs4 import BeautifulSoup


class Enru:
    def __init__(self, parser):
        self.parser = parser

    def run(self, word, show_examples):
        # TODO: throw error if there's no word

        url = self.get_url(word)
        markup = self.fetch(url)
        content = self.parse(markup, show_examples)
        return content

    def fetch(self, url):
        return urllib.urlopen(url)

    def parse(self, markup, show_examples):
        soup = BeautifulSoup(markup, "lxml")
        return self.parser.get_content(soup, show_examples)

    def get_url(self, word):
        return self.parser.get_url(word)
