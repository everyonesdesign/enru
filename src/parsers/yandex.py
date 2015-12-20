#coding=utf-8
from termcolor import colored

class YandexParser:
    def get_url(self, word):
        base = "https://slovari.yandex.ru/"
        tail = "{word}/перевод/".format(word=word)
        return base + tail

    def get_content(self, soup):
        title = soup.find(class_="b-translation__title")

        # word exists
        if title:
            title_word = title.find(class_="b-translation__text")
            title_pronunciation = title.find(class_="b-translation__tr")

            groups = soup.select(".b-translation__group")

            self.print_tag(title_word, attrs=["bold"])
            self.print_tag(title_pronunciation, color="blue")

            self.add_space()
            
            for group in groups:
                group_title = group.find(class_="b-translation__group-title")
                translation = group.find(class_="b-translation__translation-words")
                examples = group.find_all(class_="b-translation__example")

                self.print_tag(group_title, color="yellow")
                self.print_tag(translation)

                # TODO: make examples optional
                # for example in examples:
                #     example.find(class_="b-translation__src-num").extract()
                #     self.print_tag(example)

                self.add_space()

        # nothing found
        else:
            print(colored("Ничего не найдено", "red"))

    # print
    def print_tag(self, tag, color=None, attrs=[]):
        if tag:
            text = tag.get_text().encode("utf-8")
            if color or attrs:
                print(colored(text, color=color, attrs=attrs))
            else:
                print(text)

    def add_space(self):
        print("")

