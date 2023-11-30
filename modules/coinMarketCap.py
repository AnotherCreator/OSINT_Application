from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class CoinMarketCapApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.coin_list = []

    def get_exchange_rate(self):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        url_metadata = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/info"

        parameters = {
            'start': '1',
            'limit': '100',
            'convert': 'USD',
            "aux": "cmc_rank"
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_key,
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            coins = data["data"]

            for x in coins:
                new_coin = [x["symbol"],  # Coin Abbreviation
                            x["name"],  # Coin Full Name
                            x["quote"]["USD"]["price"],  # Coin Price
                            x["quote"]["USD"]["percent_change_24h"]]  # Daily % Change
                self.coin_list.append(new_coin)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

    def get_coin(self, abbreviation):
        for x in self.coin_list:
            if x[0] == abbreviation:
                return x

