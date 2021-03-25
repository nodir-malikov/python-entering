import json
from pprint import pprint

import googlemaps

# XAXA!!! Google Api key = AIzaSyDKJIH7Ywy7JzOcsm9NhbpiRnCraSx5Dzk

gmaps = googlemaps.Client(key='AIzaSyDKJIH7Ywy7JzOcsm9NhbpiRnCraSx5Dzk')

data = gmaps.geocode('Yangiabad Str, Shayxontohur tumani, Toshkent')  # Qidirilayotgan adres

data = json.dumps(data)  # json formatda otvet oldik

file = 'place.json'
with open(file, 'w') as f:  # olingan json ni json fayl ga yozdik
    json.dump(data, f)

with open(file, 'r') as f:  # json ni o'qiyapmiz
    data = json.load(f)  # String formatda o'qiladi

print(type(data))  # type = str
data = json.loads(data)  # json formatga o'tkazyapmiz
print(type(data))  # type = json

# print(json.dumps(data, indent=4))  # indent = 4 bizga json ni chiroyli qilib chiqarib beradi
kenglik = data[0]['geometry']['location']['lat']
uzunlik = data[0]['geometry']['location']['lng']
# json ni ichidan kenglik va uzunlikni oldik
print(f'{kenglik}, {uzunlik}')
