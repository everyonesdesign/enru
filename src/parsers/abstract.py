from abc import ABCMeta, abstractmethod


class AbstractParser:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_url(self):
        pass

    @abstractmethod
    def get_content(self):
        pass