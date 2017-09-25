import unittest
from finance.config import Config
from finance.currency import Currency
from finance.exception.invalidConfigurationException import InvalidConfigurationException

class TestConfig(unittest.TestCase):

    def test_no_currencies_loaded_by_default(self):
        config = Config('')
        self.assertEqual([], config.currencies)

    def test_it_can_load_currencies(self):
        config = Config('test/resources/config.json')
        config.load()

        self.assertTrue(any(listedCurrency.symbol == "XRP" for listedCurrency in config.currencies))
        self.assertTrue(any(listedCurrency.symbol == "XVG" for listedCurrency in config.currencies))

    def test_it_can_throw_invalid_configuration_exception(self):
        config = Config('test/resources/config_invalid.json')
        with self.assertRaises(InvalidConfigurationException) as context:
            config.load()

        self.assertTrue('there seems to be a problem with your configuration: double check value at token: XRP' in str(context.exception))