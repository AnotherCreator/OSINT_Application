from dotenvy import load_env, read_file
import os

from modules.coinMarketCap import CoinMarketCapApi
from modules.exchangeRate import ExchangeRateApi

# Load API Secrets
load_env(read_file('.env'))
EXCHANGE_RATE_API_SECRET = os.environ.get("EXCHANGE_RATE_API_SECRET")
COIN_MARKET_CAP_API_SECRET = os.environ.get("COIN_MARKET_CAP_API_SECRET")

# Create an instance of the ExchangeRateApi class
exchange_rate_api = ExchangeRateApi(EXCHANGE_RATE_API_SECRET)
coin_market_cap_api = CoinMarketCapApi(COIN_MARKET_CAP_API_SECRET)

# EXCHANGE RATE API SECTION

# Base currency
base_currency = 'USD'

# Get the exchange rates for USD with all available currencies
exchange_rates = exchange_rate_api.get_exchange_rates(base_currency)

if exchange_rates:
    print(f'Exchange rates for {base_currency}:')
    for target_currency, rate in exchange_rates.items():
        print(f'{base_currency} to {target_currency}: {rate}')

# COIN MARKET CAP API SECTION
coin_market_cap_api.get_exchange_rate()
