import json

class Currency:

    def __init__(self, symbol):
        self.__symbol = symbol
        self.__tokens = []
        self.buyValue = 0
        self.sellValue = 0

    @property
    def symbol(self):
        return self.__symbol

    def label(self):
        config = json.loads(open('config/config.json').read())
        return config['known_coins'][self.symbol]

    def addTokens(self, amount, price):
        self.__tokens += [{"amount": amount, "price": price}]

    def count(self):
        number_of_coins = 0
        for index in range(0, len(self.__tokens)):
            number_of_coins += self.__tokens[index]["amount"]

        return number_of_coins

    def average(self):
        value = 0.0
        number_of_coins = 0

        if value == len(self.__tokens):
            return value

        for index in range(0, len(self.__tokens)):
            value           += self.__tokens[index]["price"]
            number_of_coins += self.__tokens[index]["amount"]

        return float(value) / float(number_of_coins)