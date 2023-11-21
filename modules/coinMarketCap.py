from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class CoinMarketCapApi:
    def __init__(self, api_key):
        self.api_key = api_key

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
            print(data)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
