import unittest
import requests_mock
from finance.broker.litebit import Litebit
from finance.currency import Currency


class liteBitTest(unittest.TestCase):

    @requests_mock.mock()
    def test_if_data_can_be_processed(self, mocked_request):
        with open('test/resources/buy.html', 'r') as content_file:
            mocked_request.get('https://www.litebit.eu/en/buy', text=content_file.read())

        with open('test/resources/sell.html', 'r') as content_file:
            mocked_request.get('https://www.litebit.eu/en/sell', text=content_file.read())

        bitcoin = Currency("BTC")
        ripple  = Currency("XRP")
        exchange = Litebit([bitcoin,ripple])
        currencies = exchange.fetch_token_data()
        self.assertEqual(currencies[0].buyValue, ("%.6f" % 2812.800000))
        self.assertEqual(currencies[0].sellValue, ("%.6f" % 2694.910000))
        self.assertEqual(currencies[1].buyValue, ("%.6f" % 0.159777))
        self.assertEqual(currencies[1].sellValue, ("%.6f" % 0.142453))