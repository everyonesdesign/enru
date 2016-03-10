class Enru:
    def __init__(self, parser):
        self.parser = parser

    def run(self, word, **kwargs):
        return self.parser.run(word)
