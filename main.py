from exchangeRate import ExchangeRateApi

api_key = '3ca2c032b93f6bfff74ec55c'

# Create an instance of the ExchangeRateApi class
exchange_rate_api = ExchangeRateApi(api_key)

# Base and target currencies
base_currency = 'USD'
target_currencies = ['EUR', 'CNY', 'GBP', 'JPY', 'CHF']

# Get the exchange rate
for target_currency in target_currencies:
    rate = exchange_rate_api.get_exchange_rate(base_currency, target_currency)
    if rate is not None:
        print(f'{base_currency} to {target_currency}: {rate}')