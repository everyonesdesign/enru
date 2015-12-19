#!/usr/bin/env python
#coding=utf-8
import urllib
import sys

from termcolor import colored

from bs4 import BeautifulSoup

# get basic info
word = sys.argv[1]
base = "https://slovari.yandex.ru/"
tail = "{word}/перевод/".format(word=word)
url = base + tail

#fetch
response = urllib.urlopen(url)

# parse
soup = BeautifulSoup(urllib.urlopen(url), "lxml")
title = soup.find(class_="b-translation__title")

# word exists
if title:
    title_word = title.find(class_="b-translation__text")
    title_pronunciation = title.find(class_="b-translation__tr")

    groups = soup.select(".b-translation__group")

    # print
    def print_tag(tag, color=None, attrs=[]):
        if tag:
            text = tag.get_text().encode("utf-8")
            if color or attrs:
                print(colored(text, color=color, attrs=attrs))
            else:
                print(text)

    def add_space():
        print("")

    print_tag(title_word, attrs=["bold"])
    print_tag(title_pronunciation, color="blue")

    add_space()
    
    for group in groups:
        group_title = group.find(class_="b-translation__group-title")
        translation = group.find(class_="b-translation__translation-words")
        examples = group.find_all(class_="b-translation__example")

        print_tag(group_title, color="yellow")
        print_tag(translation)

        # TODO: make examples optional
        # for example in examples:
        #     example.find(class_="b-translation__src-num").extract()
        #     print_tag(example)

        add_space()

# nothing found
else:
    print(colored("Ничего не найдено", "red"))
