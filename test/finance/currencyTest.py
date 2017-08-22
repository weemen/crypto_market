import unittest
from finance.currency import Currency


class TestCurrency(unittest.TestCase):

    def test_currency_properties(self):
        myCurrency = Currency("BTC")
        myCurrency.buyValue = 2.5
        myCurrency.sellValue = 2.1
        self.assertEqual(myCurrency.symbol,"BTC")
        self.assertEqual(myCurrency.label(), "Bitcoin")
        self.assertEqual(myCurrency.buyValue, 2.5)
        self.assertEqual(myCurrency.sellValue, 2.1)

    def test_average_token_calculation_with_no_input(self):
        myCurrency = Currency("BTC")
        self.assertEqual(myCurrency.average(), 0)

    def test_avarage_token_calculation_with_token_input(self):
        myCurrency = Currency("BTC")
        myCurrency.buyValue = 0
        myCurrency.sellValue = 0
        myCurrency.addTokens(10, 2.0)
        myCurrency.addTokens(10, 4.0)
        self.assertEqual(myCurrency.average(), 0.3)

    def test_it_counts_zero_tokens_when_no_tokens_are_set(self):
        myCurrency = Currency("BTC")
        myCurrency.buyValue = 0
        myCurrency.sellValue = 0

        self.assertEquals(myCurrency.count(), 0)

    def test_it_counts_20_tokens_when_20_tokens_are_set(self):
        myCurrency = Currency("BTC")
        myCurrency.buyValue = 0
        myCurrency.sellValue = 0
        myCurrency.addTokens(2, 1.0)
        myCurrency.addTokens(3, 2.0)
        myCurrency.addTokens(15, 3.0)

        self.assertEqual(myCurrency.count(), 20)
