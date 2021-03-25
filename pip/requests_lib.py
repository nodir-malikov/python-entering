import requests
from pprint import pprint

# # Kun.uz saytini source kodini tortib olish
# manzil = "https://kun.uz/news/main"
# r = requests.get(manzil)
# pprint(r.text)

# Davlat poytaxtini aniqlash
country = "Uzbekistan"
url = f"https://restcountries.eu/rest/v2/name/{country}"
r = requests.get(url)
r_json = r.json()[0]
print(r_json['capital'])
