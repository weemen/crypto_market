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

        currency_xrp = Currency('XRP')
        currency_xrp.addTokens(250, 55.42)
        currency_xvg = Currency('XVG')
        currency_xvg.addTokens(10000, 42.99)
        currency_xvg.addTokens(25000, 101.25)

        self.assertEqual(currency_xrp.symbol, config.currencies[0].symbol)
        self.assertEqual(currency_xrp.average(), config.currencies[0].average())
        self.assertEqual(currency_xvg.symbol, config.currencies[1].symbol)
        self.assertEqual(currency_xvg.average(), config.currencies[1].average())


    def test_it_can_throw_invalid_configuration_exception(self):
        config = Config('test/resources/config_invalid.json')
        with self.assertRaises(InvalidConfigurationException) as context:
            config.load()

        self.assertTrue('there seems to be a problem with your configuration: double check value at token: XRP' in str(context.exception))