from datetime import datetime


### Qiymat qaytarmaydi bular ###
def salom_ber():
    """Salom beruvchi funksiya"""  # Bu DOCSTRING, ya'ni funcsiyaga dokumentatsiya
    print("Assalomu alaykum!")


def salom_ber_ism(ism):
    """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")


def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")


def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {datetime.now().year - tugilgan_yil} yoshda")


def yosh_hisobla_ismsiz(tugilgan_yil, joriy_yil=datetime.now().year):  # joriy yil uchun st.qiymat 2020
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz")


### Bular qiymat qaytaradi ###
def toliq_ism_yasa(ism, familiya):
    """Toliq isma qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()  # qiymat qaytarish uchun return operatorini ishlatamiz


# Ixtiyoriy argumentli funksiya
def toliq_ism_yasa_2(ism, familiya, otasining_ismi=''):
    """Toliq isma qaytaruvchi funksiya"""
    if otasining_ismi:  # otasining_ismi mavjudligini tekshiramiz
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()


# Lug'at qaytaramiz
def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya': kompaniya,
            'model': model,
            'rang': rangi,
            'korobka': korobka,
            'yil': yili,
            'narh': narhi}
    return avto


# Ro'yxat qaytaramiz
def oraliq(min, max, qadam=None):
    sonlar = []  # bo'sh ro'yxat
    while min < max:
        sonlar.append(min)
        if qadam is None:
            min += 1
        else:
            min += qadam
    return sonlar


# Ro'yxat uzatish
def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar


########################

salom_ber()
print()
salom_ber_ism('Nodir')
print()
toliq_ism('Nodir', 'Malikov')
print()
yosh_hisobla('Nodir', 2004)
print()
yosh_hisobla_ismsiz(2004)

########################
print()
#
talaba1 = toliq_ism_yasa('olim', 'hakimov')
talaba2 = toliq_ism_yasa('hakim', 'olimov')

print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
#
print()
#
talaba1 = toliq_ism_yasa_2('olim', 'hakimov')  # otasining_ismi kiritilmadi
talaba2 = toliq_ism_yasa_2('hakim', 'olimov', 'abrorovich')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

###
print()
###
avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2016, 15000)
avtolar = [avto1, avto2]
print('Onlayn bozordagi mavjud avtomashinalar:')
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

###
print()
###
print(oraliq(0, 10))
print(oraliq(10, 21))
print(oraliq(0, 21, 2))  # 0 dan 21 gacha 2 qadam bilan
###
print()
###
###
###
print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar = []  # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting", end='')
    kompaniya = input("Ishlab chiqaruvchi: ")
    model = input("Modeli: ")
    rangi = input("Rangi: ")
    korobka = input("Korobka: ")
    yili = input("Ishlab chiqarilgan yili: ")
    narhi = input("Narhi: ")

    # Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida
    # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))

    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob == 'no':
        break

print('Salonimizdagi avtolar:')
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. {avto[korobka]} korobka. Narhi: {narh}")

###
print()
###
talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
