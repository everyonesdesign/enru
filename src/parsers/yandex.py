#coding=utf-8
from termcolor import colored

from abstract import AbstractParser


class YandexParser(AbstractParser):
    def get_url(self, word):
        base = "https://slovari.yandex.ru/"
        tail = "{word}/перевод/".format(word=word)
        return base + tail

    def get_content(self, soup, show_examples):
        content = ""
        title = soup.find(class_="b-translation__title")

        # word exists
        if title:
            title_word = title.find(class_="b-translation__text")
            title_pronunciation = title.find(class_="b-translation__tr")

            groups = soup.select(".b-translation__group")

            content += self.get_tag(title_word, attrs=["bold"])
            content += self.get_tag(title_pronunciation, color="blue")

            for group in groups:
                content += self.process_group(group, show_examples)

        # nothing found
        else:
            print(colored("Ничего не найдено", "red"))

        return content

    def process_group(self, group, show_examples):
        content = self.get_space()

        group_title = group.find(class_="b-translation__group-title")
        translation = group.find(class_="b-translation__translation-words")
        examples = group.find_all(class_="b-translation__example")

        if group_title:
            content += self.get_tag(group_title, color="yellow")
        if translation:
            content += self.get_tag(translation)

        if show_examples:
            for example in examples:
                example.find(class_="b-translation__src-num").extract()
                self.get_tag(example, color='green')

        return content

    def get_tag(self, tag, color=None, attrs=[]):
        result = ""

        if tag:
            text = tag.get_text().encode("utf-8")
            if color or attrs:
                result = colored(text, color=color, attrs=attrs)
            else:
                result = text

        result += self.get_space()
        return result

    def get_space(self):
        return "\n"
