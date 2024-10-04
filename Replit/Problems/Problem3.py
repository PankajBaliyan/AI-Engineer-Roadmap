# 3. Install an external module and use it to perform an operation of your interest.
import requests


def Main():
    # Call the function
    fetch_data()


# Function to fetch data from a public API
def fetch_data():
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        print('Fetched Data:', data)
    else:
        print(f'Failed to fetch data. Status code: {response.status_code}')
