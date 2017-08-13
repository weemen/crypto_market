from abc import ABCMeta, abstractmethod


class Broker:
    __metaclass__ = ABCMeta

    def __init__(self, currencies):
        self._tokens = currencies

    def tokens(self):
        return self._tokens

    @abstractmethod
    def fetch_token_data(self):
        pass