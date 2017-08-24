import json

from finance.currency import Currency
from finance.exception.invalidConfigurationException import InvalidConfigurationException

class Config:

    def __init__(self, config_file):
        self.__config_file = config_file
        self.__currencies = []

    @property
    def currencies(self):
        return self.__currencies

    def load(self):
        #'config/config.json'
        config = json.loads(open(self.__config_file).read())
        for token in config['inventory']:
            currency = Currency(token)
            for inventory in config['inventory'][token]['inventory']:
                try:
                    currency.addTokens(int(inventory['amount']), float(inventory['buyValue']))
                except ValueError:
                    raise InvalidConfigurationException(("there seems to be a problem with your configuration: double check value at token: %s" % token));

            self.__currencies += [currency]