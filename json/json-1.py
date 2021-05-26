import json
from pprint import pprint

import googlemaps

# XAXA!!! Google Api key = AIzaSyDKJIH7Ywy7JzOcsm9NhbpiRnCraSx5Dzk
# XAXA!!! Google Api key = AIzaSyCNoILb2Qa6_Trfhlq0pjNqwaWN9vGMKJk
import requests

GMAPS_API_KEY = 'AIzaSyDKJIH7Ywy7JzOcsm9NhbpiRnCraSx5Dzk'

# gmaps = googlemaps.Client(key=f'{GMAPS_API_KEY}')
#
# # data = gmaps.geocode('Yangiabad Str, Shayxontohur tumani, Toshkent')  # Qidirilayotgan adres
# data = gmaps.geocode('Yangiabad Str, Shayxontohur tumani, Toshkent')  # Qidirilayotgan adres
#
# data = json.dumps(data)  # json formatda otvet oldik
#
# file = 'place.json'
# with open(file, 'w') as f:  # olingan json ni json fayl ga yozdik
#     json.dump(data, f)
#
# with open(file, 'r') as f:  # json ni o'qiyapmiz
#     data = json.load(f)  # String formatda o'qiladi
#
# print(type(data))  # type = str
# data = json.loads(data)  # json formatga o'tkazyapmiz
# print(type(data))  # type = json
#
# # print(json.dumps(data, indent=4))  # indent = 4 bizga json ni chiroyli qilib chiqarib beradi
# kenglik = data[0]['geometry']['location']['lat']
# uzunlik = data[0]['geometry']['location']['lng']
# # json ni ichidan kenglik va uzunlikni oldik
# print(f'{kenglik}, {uzunlik}')


# NEARBY SEARCH -- Yaqin atrofdagi joylarni topish ====================================================

# Masjidlarni topamiz
mosque_near_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={GMAPS_API_KEY}&' \
         f'location=41.3069358,69.2284315&' \
         f'type=mosque&name=мечеть&keyword=мечеть&language=ru&rankby=distance'

# response = json.loads(json.dumps(requests.post(nearby).json(), indent=4, ensure_ascii=False))
# response = [i['name'] for i in response['results']]
# print(response)

response = [mosque['name'] for mosque in json.loads(json.dumps(requests.post(mosque_near_url).json()['results'],
                                                               ensure_ascii=False))]
# print(response)

for i in response:
    print(i)
