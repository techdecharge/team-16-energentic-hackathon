import requests
from app.config import WORLD_ENGINE_URL

url = f"{WORLD_ENGINE_URL}/utility/detailed"

payload = ""
headers = {
  'Content-Type': 'application/json'
}


def fetch_company_details(company_name):
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text
