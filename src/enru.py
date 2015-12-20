import urllib

from bs4 import BeautifulSoup


class Enru:
    def __init__(self, parser):
        self.parser = parser

    def run(self, word):
        # TODO: throw error if there's no word

        url = self.get_url(word)
        markup = self.fetch(url)
        content = self.parse(markup)
        return content

    def fetch(self, url):
        return urllib.urlopen(url)

    def parse(self, markup):
        soup = BeautifulSoup(markup, "lxml")
        return self.parser.get_content(soup)

    def get_url(self, word):
        return self.parser.get_url(word)
