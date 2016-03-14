import unittest
from urllib.error import URLError

from bs4 import BeautifulSoup

from ..adapters.yandex import YandexAdapter


class YandexAdapterTestCase(unittest.TestCase):
    def setUp(self):
        self.adapter = YandexAdapter(show_examples=False)

    def test_get_url(self):
        self.assertEqual(
            self.adapter.get_url('test'),
                'https://slovari.yandex.ru/test' +
                '/%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4/'
            )

    def test_get_content_without_examples(self):
        with open("markup.html", "r") as file:
            markup = file.read()

            soup = BeautifulSoup(markup, "lxml")
            result = self.adapter.get_content(soup)

            self.assertTrue("испытание" in result)
            self.assertTrue("проба" in result)
            self.assertTrue("мерило" in result)
            self.assertTrue("пробный камень" in result)

            self.assertFalse("nuclear tests" in result)
            self.assertFalse("ядерные испытания" in result)
            self.assertFalse("strength test" in result)
            self.assertFalse("испытание на прочность" in result)

    def test_get_content_with_examples(self):
        self.adapter = YandexAdapter(show_examples=True)

        with open("markup.html", "r") as file:
            markup = file.read()

            soup = BeautifulSoup(markup, "lxml")
            result = self.adapter.get_content(soup)

            self.assertTrue("испытание" in result)
            self.assertTrue("проба" in result)
            self.assertTrue("мерило" in result)
            self.assertTrue("пробный камень" in result)

            self.assertTrue("nuclear tests" in result)
            self.assertTrue("ядерные испытания" in result)
            self.assertTrue("strength test" in result)
            self.assertTrue("испытание на прочность" in result)

    def test_run(self):
        """
        Actual Yandex markup launch
        Will not be executed if there's no network connection
        """

        try:
            result = self.adapter.run("test")

            self.assertTrue("испытание" in result)
            self.assertTrue("проба" in result)
            self.assertTrue("мерило" in result)
            self.assertTrue("пробный камень" in result)

            self.assertFalse("nuclear tests" in result)
            self.assertFalse("ядерные испытания" in result)
            self.assertFalse("strength test" in result)
            self.assertFalse("испытание на прочность" in result)

        except URLError:
            raise URLError(
                """
                Network connection error during the tests
                No tests requiring network connection will be run
                """
            )



if __name__ == '__main__':
    unittest.main()
