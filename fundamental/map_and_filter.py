# map() FUNKSIYASI Bu funksiya argument sifatida ro'yxat (yoki lug'at) va boshqa bir funksiyani qabul qilib,
# ro'yxat elementlariga qabul qilingan funksya yordamida ishlov beradi. Tushunarli bo'lish uchun quyidagi misolni
# ko'ramiz.

from math import sqrt

sonlar = list(range(11))  # 0 dan 10 gacha sonlar ro'yxati
ildizlar = list(map(sqrt, sonlar))  # sonlar ro'yxatidagi barcha sonlarni ildizini hisoblab beradi va yana boshqa
# ro'yxatga joylaydi

# map() funksiyasi map obyekt qaytargani sababli, qaytgan obyektni ro'yxatga o'tkazib olish uchun list()
# funksiyasidan foyydalandik.

print(ildizlar)

#############
print()
###
sonlar = list(range(11))  # 0 dan 10 gacha sonlar ro'yxati


def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x * x


print(list(map(daraja2, sonlar)))  # sonlar ning kvadratini hisoblaymiz

print()
###################
# Endi huddi shu lambda bilan
###################
kvadratlar = list(map(lambda x: x * x, sonlar))
print(kvadratlar)

###
print()
###
### Map bo'lmaganida biz shunday ko'rinishda yozishimiz kerak bo'lar edi.
kvadratlar = []
for son in sonlar:
    kvadratlar.append(son * son)
print(kvadratlar)

###
print()
###
# map() funksiyasiga bir nechta ro'yxatlar ham uzatish mumkin:
a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x, y: x + y, a, b))
print(a_plus_b)

###
print()
###
ismlar = ['hasan', 'husan', 'olim', 'umid']
print(list(map(lambda matn: matn.upper(), ismlar)))

print()
print()
print()
# ################################################################################################### filter()
# FUNKSIYASI Bu funksiya ham argument sifatida ro'yxat va boshqa funskiyani qabul qilib oladi va berilgan ro'yxat
# elementlarini berilgan funksiya yordamida saralaydi. Bunda argument sifatida uzatilgan funksiya mantiqiy qiymat
# qaytarishi kerak (True yoki False).
import random as r

sonlar = r.sample(range(100), 10)  # 0-99 oralig'ida 10 ta tasodifiy sonlar


def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
    return x % 2 == 0


juft_sonlar = list(filter(juftmi, sonlar))
print(sonlar)
print(juft_sonlar)

########### huddi shu LAMBDA orqali ############

sonlar = r.sample(range(100), 10)  # 0-99 oralig'ida 10 ta tasodifiy sonlar
juft_sonlar = list(filter(lambda son: son % 2 == 0, sonlar))

print(sonlar)
print(juft_sonlar)

##############
print()
print()
##############
mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", "tarvuz", "qovun", "banan"]

mevalar_b = list(filter(lambda meva: meva.startswith('b'), mevalar))
# Quyidagi dastur mevalar ro'yxatidan b harfiga boshlanuvchi mevalarni ajratib oladi
print(mevalar_b)

###########
print()
print()

###########
mevalar2 = list(filter(lambda meva: len(meva) <= 5, mevalar))
# Quyidagi dastur esa mevalar ro'yxatidan nomi 5 yoki undan kam harfdan iborat mevalarni saralab oladi.
print(mevalar2)

######
print()
print()
######
natija = list(filter(lambda meva: (meva.startswith('a') and meva.endswith('r')), mevalar))
# Quyidagi dastur 'a' bilan boshlanib, 'r' bilan tugaydigan so'zlarni topadi.
print(natija)
