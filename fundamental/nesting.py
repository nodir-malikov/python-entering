car0 = {
    'model': 'lacetti',
    'rang': 'oq',
    'yil': 2018,
    'narh': 13000,
    'km': 50000,
    'korobka': 'avtomat'
}

car1 = {
    'model': 'nexia 3',
    'rang': 'qora',
    'yil': 2015,
    'narh': 9000,
    'km': 89000,
    'korobka': 'mexanika'
}

car2 = {
    'model': 'gentra',
    'rang': 'qizil',
    'yil': 2019,
    'narh': 15000,
    'km': 20000,
    'korobka': 'mexanika'
}

cars = [car0, car1, car2]  # Ro'yxat barcha lug'atlarni(obyektlarni) joyladik

for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang, "
          f"{car['yil']}-yil, {car['narh']}$")

print(cars[0])
print(cars[0]['model'])
print(f"{cars[2]['rang'].title()} "
      f"{cars[2]['model']}")

malibus = []  # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
for n in range(10):
    new_car = {  # har bir yangi mashina uchun lug'at yaratamiz
        'model': 'malibu',
        'rang': None,  # rangi noaniq
        'yil': 2020,
        'narh': None,  # narhi belgilanmagan
        'km': 0,
        'korobka': 'avto'
    }
    malibus.append(new_car)  # yangi lug'atni ro'yxatga qo'shamiz

for malibu in malibus[:3]:
    malibu['rang'] = 'qora'

for malibu in malibus[3:6]:
    malibu['rang'] = 'oq'

for malibu in malibus[6:]:  # ohirgi 4 ta mashinani
    malibu['rang'] = 'qizil'  # rangi qora
    malibu['korobka'] = 'mexanika'  # korobkasi mexanika

for malibu in malibus:
    if malibu['korobka'] == 'avto':
        malibu['narh'] = 40000
    else:
        malibu['narh'] = 35000

for i in malibus:
    print(f"{i['model'].title()}, "
          f"{i['rang']} rang, "
          f"{i['yil']}-yil, "
          f"{i['narh']}$")

###
print()
###
# LUG'AT ICHIDA RO'YXAT

devs = {
    'ali': ['python', 'c++'],
    'nodir': ['java', 'python'],
    'qodir': ['php']
}

for ism, tillar in devs.items():
    print(f"\n{ism.title()} dasturchimiz shu tillarni biladi:", end='')
    for til in tillar:
        print(f'{til.upper()}', end='')
print()

###
# LUG'AT ICHIDA LUG'AT
hamkasblar = {
    'ali': {'familiya': 'valiyev',
            'tyil': 1995,
            'malumot': 'oliy',
            'tillar': ['python', 'c++']
            },
    'vali': {'familiya': 'aliyev',
             'tyil': 2001,
             'malumot': "o'rta-maxsus",
             'tillar': ['html', 'css', 'js']},
    'hasan': {'familiya': 'husanov',
              'tyil': 1999,
              'malumot': 'maxsus',
              'tillar': ['python', 'php']}
}

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())
# Lug'at ichidagi lug'atlar bir hil tuzilishga ega bo'lgani ishingizni ancha yengillashtiradi, aks holda kodingiz
# murakkablashib ketishi mumkin.
print()
print()
# Amaliyot
davlatlar = {
    "o'zbekiston": {'poytaxt': "toshkent",
                    'maydon': 448978,
                    'aholi': 33_000_000,
                    'pul birligi': "so'm"
                    },
    "rossiya": {'poytaxt': "moskva",
                'maydon': 17_098_246,
                'aholi': 144_000_000,
                'pul birligi': "rubl"
                },
    "aqsh": {'poytaxt': "vashington",
             'maydon': 9_631_418,
             'aholi': 327_000_000,
             'pul birligi': "dollar"},
    "malayziya": {'poytaxt': "kuala-lumpur",
                  'maydon': 329750,
                  'aholi': 25_000_000,
                  'pul birligi': "rinngit"}
}

davlat = input('Davlat nomini kiriting: ').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")
