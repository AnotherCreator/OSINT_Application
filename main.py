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

#-------------------------------------------- EXCHANGE RATE API SECTION ------------------------------------------

# Get user input for the base currency
base_currency = input("Enter the base currency: ").upper() #all inputs are uppercase

# Get user input for the target currency
target_currency = input("Enter the target currency: ").upper() #all inputs are uppercase

# Get the exchange rate for the specified currencies
exchange_rate = exchange_rate_api.get_exchange_rates(base_currency, target_currency)

if exchange_rate is not None:
    print(f'Exchange rate from {base_currency} to {target_currency}: {exchange_rate}')
else:
    print(f'Unable to fetch exchange rate for {base_currency} to {target_currency}')

#---------------- COIN MARKET CAP API SECTION --------------------------------------
coin_market_cap_api.get_exchange_rate()

#-------------------------------------- RESTful API ----------------------------------

# Get user input for the country name
user_country = input("Enter the name of the country: ")

# Get country information based on user input
country_info = rest_countries_api.get_country_info(user_country)

if country_info:
    # Get information from the response
    name = country_info[0].get('name', {}).get('common', 'N/A')
    capital = country_info[0].get('capital', 'N/A')
    population = country_info[0].get('population', 'N/A')
    area = country_info[0].get('area', 'N/A')
    gini = country_info[0].get('gini', 'N/A')
    latlng = country_info[0].get('latlng', ['N/A', 'N/A'])
    latitude, longitude = latlng[0], latlng[1]
    independent = country_info[0].get('independent', 'N/A')
    landlocked = country_info[0].get('landlocked', 'N/A')

    # Print the information for the specified country
    print(f"\n{'Country':<50}{'Capital':<20}{'Population':<15}{'Area':<15}{'Gini Index':<15}{'Latitude':<15}{'Longitude':<15}{'Independent':<15}{'Landlocked':<15}")
    print(f"{str(name):<50}{str(capital):<20}{str(population):<15}{str(area):<15}{str(gini):<15}{str(latitude):<15}{str(longitude):<15}{str(independent):<15}{str(landlocked):<15}")

else:
    print(f"\nNo information was found for {user_country}")