import os

import requests
from dotenv import load_dotenv


load_dotenv()

USERNAME = os.getenv('BITBUCKET_USERNAME')
PASSWORD = os.getenv('BITBUCKET_PASSWORD')
BASE_URL = f'https://api.bitbucket.org/2.0/repositories/{USERNAME}/'

response = requests.get(f'{BASE_URL}', auth=(USERNAME, PASSWORD), params={'pagelen': 100})
print(response.json())
