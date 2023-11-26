from dotenvy import load_env, read_file
import os

from modules.coinMarketCap import CoinMarketCapApi
from modules.restCountryData import RestCountriesApi
from modules.exchangeRate import ExchangeRateApi

# Load API Secrets
load_env(read_file('.env'))
EXCHANGE_RATE_API_SECRET = os.environ.get("EXCHANGE_RATE_API_SECRET")
COIN_MARKET_CAP_API_SECRET = os.environ.get("COIN_MARKET_CAP_API_SECRET")

# Create an instance of the Api classes
exchange_rate_api = ExchangeRateApi(EXCHANGE_RATE_API_SECRET)
coin_market_cap_api = CoinMarketCapApi(COIN_MARKET_CAP_API_SECRET)
rest_countries_api = RestCountriesApi()

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

# RESTful API

# Get information for all countries
all_countries_info = rest_countries_api.get_all_countries_info()

if all_countries_info:
    print(f"{'Country':<50}{'Capital':<20}{'Population':<15}{'Area':<15}{'Gini Index':<15}{'Latitude':<15}{'Longitude':<15}{'Independent':<15}{'Landlocked':<15}")
    for country_info in all_countries_info:
        name = country_info.get('name', {}).get('common', 'N/A')
        capital = country_info.get('capital', [])[0] if country_info.get('capital') else 'N/A'
        population = country_info.get('population', 'N/A')
        area = country_info.get('area', 'N/A')
        gini = country_info.get('gini', 'N/A')
        latlng = country_info.get('latlng', ['N/A', 'N/A'])
        latitude, longitude = latlng[0], latlng[1]
        independent = country_info.get('independent', 'N/A')
        landlocked = country_info.get('landlocked', 'N/A')

        # Print the information for each country
        print(f"{str(name):<50}{str(capital):<20}{str(population):<15}{str(area):<15}{str(gini):<15}{str(latitude):<15}{str(longitude):<15}{str(independent):<15}{str(landlocked):<15}")
