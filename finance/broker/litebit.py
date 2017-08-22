from finance.broker.broker import Broker
from lxml import html
import cfscrape

class Litebit(Broker):

    TOKEN_MAPPING = {
        "BTC":"rate-tile-bitcoin",
        "STRAT":"rate-tile-stratis",
        "XRP":"rate-tile-ripple",
        "XVG":"rate-tile-verge"
    }

    def __init__(self, currencies):
        super(Litebit, self).__init__(currencies)
        self.__paths = []
        self.__currencies = currencies
        self.__scraper = cfscrape.create_scraper()

    def fetch_token_data(self):
        self.__currencies = list(self.load_prices(currency, self.TOKEN_MAPPING[currency.symbol]) for currency in self.__currencies if currency.symbol in self.TOKEN_MAPPING)
        return self.__currencies

    def load_prices(self, currency, litebit_element_id):
        buying_page = self.get_buying_page()
        selling_page = self.get_selling_page()
        xpath = "//*[@id=\"%s\"]/small/span/text()" % litebit_element_id
        currency.buyValue = html.fromstring(buying_page).xpath(xpath)[0].strip().replace(',', '')
        currency.sellValue = html.fromstring(selling_page).xpath(xpath)[0].strip().replace(',', '')
        return currency

    def get_buying_page(self):
        return self.__scraper.get('https://www.litebit.eu/en/buy', allow_redirects=True).content

    def get_selling_page(self):
        return self.__scraper.get('https://www.litebit.eu/en/sell', allow_redirects=True).content