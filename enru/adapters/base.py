from urllib import request
from urllib.parse import quote

from bs4 import BeautifulSoup

from ..exceptions import NothingFoundException

class BaseAdapter:
    # template method for adapter launch
    def run(self, word):
        url = self.get_url(quote(word))
        markup = self.fetch(url)

        try:
            content = self.parse(markup)
        except NothingFoundException:
            content = "Слово «{word}» не найдено".format(word=word)

        return content

    def fetch(self, url):
        return request.urlopen(url)

    def parse(self, markup):
        soup = BeautifulSoup(markup, "lxml")
        return self.get_content(soup)

    # abstract methods
    def get_url(self, word):
        raise NotImplementedError

    def get_content(self, soup):
        raise NotImplementedError
