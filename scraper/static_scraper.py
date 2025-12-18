import requests
from bs4 import BeautifulSoup

URL = "https://www.greenhouse.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.text[:1000])
