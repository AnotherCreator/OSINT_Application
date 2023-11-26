import requests

class RestCountriesApi:
    def __init__(self):
        self.base_url = 'https://restcountries.com/v3.1'

    def get_all_countries_info(self):
        api_url = f'{self.base_url}/all'

        try:
            response = requests.get(api_url)
            data = response.json()

            if response.status_code == 200:
                return data
            else:
                print(f'Error: {data.get("error", "Unknown error")}')
        except Exception as e:
            print(f'An error occurred: {str(e)}')

        return None