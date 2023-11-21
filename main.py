from dotenvy import load_env, read_file
from exchangeRate import ExchangeRateApi
import os

# Load API Secrets
load_env(read_file('.env'))
EXCHANGE_RATE_API_SECRET = os.environ.get("EXCHANGE_RATE_API_SECRET")

# Create an instance of the ExchangeRateApi class
exchange_rate_api = ExchangeRateApi(EXCHANGE_RATE_API_SECRET)

# Base and target currencies
base_currency = 'USD'
target_currencies = ['EUR', 'CNY', 'GBP', 'JPY', 'CHF']

# Get the exchange rate
for target_currency in target_currencies:
    rate = exchange_rate_api.get_exchange_rate(base_currency, target_currency)
    if rate is not None:
        print(f'{base_currency} to {target_currency}: {rate}')