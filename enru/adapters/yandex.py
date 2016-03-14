from urllib.parse import quote

from termcolor import colored

from .base import BaseAdapter
from ..exceptions import NothingFoundException


class YandexAdapter(BaseAdapter):
    def __init__(self, **kwargs):
        self.show_examples = kwargs["show_examples"]

    def get_url(self, word):
        base = "https://slovari.yandex.ru/"
        tail = "{word}/%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4/".format(
                        word=word)
        return base + tail

    def get_content(self, soup):
        content = ""
        title = soup.find(class_="b-translation__title")

        # word exists
        if title:
            title_word = title.find(class_="b-translation__text")
            title_pronunciation = title.find(class_="b-translation__tr")

            groups = soup.find_all(class_="b-translation__group")

            content += self.get_tag(title_word, attrs=["bold"])
            content += self.get_tag(title_pronunciation, color="blue")

            for group in groups:
                content += self.process_group(group)

        # nothing found
        else:
            raise NothingFoundException()

        return content

    def process_group(self, group):
        content = self.get_space()

        group_title = group.find(class_="b-translation__group-title")
        if group_title:
            content += self.get_tag(group_title, color="yellow")

        entries = group.find_all(class_="b-translation__entry")

        for entry in entries:
            translation = entry.find(class_="b-translation__translation-words")
            examples = entry.find_all(class_="b-translation__example")

            if translation:
                content += self.get_tag(translation)

            if self.show_examples:
                for example in examples:
                    example.find(class_="b-translation__src-num").extract()
                    content += self.get_tag(example, color='green')
                content += self.get_space()

        return content

    def get_tag(self, tag, color=None, attrs=[]):
        result = ""

        if tag:
            text = tag.get_text()
            if color or attrs:
                result = colored(text, color=color, attrs=attrs)
            else:
                result = text

        result += self.get_space()
        return result

    def get_space(self):
        return "\n"
