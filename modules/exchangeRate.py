import requests

class ExchangeRateApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://open.er-api.com/v6'

    def get_exchange_rates(self, base_currency):
        api_url = f'{self.base_url}/latest/{base_currency}?apikey={self.api_key}'

        try:
            response = requests.get(api_url)
            data = response.json()

            if response.status_code == 200:
                rates = data.get('rates')
                if rates is not None:
                    return rates
                else:
                    print('No exchange rates found.')
            else:
                print(f'Error: {data.get("error", "Unknown error")}')
        except Exception as e:
            print(f'An error occurred: {str(e)}')

        return None
