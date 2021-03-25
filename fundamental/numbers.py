from typing import Final
from datetime import datetime

float_number = 3.14
integer_number = 4
###
# UZUN SONLARNI KIRITISH
# Uzun sonlarni kiritishda, qulaylik uchun, raqamlarni pastki chiziq (_) yordamida guruhlash mumkin.
# Python - son tarkibidagi pastki chiziqlarni (_) inobatga olmasdan, uzun sonligicha qabul qiladi.
aholi_soni = 7_594_000_000  # o'zmizga qulay bo'lishi uchun shinday yozdik
print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")
###
PI: Final = 3.14
# Pythonda constanta qilish majburiy emas, ogohlantirish uchun esa *: Final ishlatilishi mumkin. Python 3.8 dan boshlab
print(PI)
PI = 5  # 'PI' is 'Final' and could not be reassigned
print(PI)
###
# BIR NECHTA O'ZGARUVCHIGA QIYMAT BERISH
x, y, z = 10, -7.25, -30
print(x, y, z)
# ## TYPECASTING IN PYTHON
# str()— int yoki float turidagi sonlarni matnga o'zgartiradi.
# int()— matn yoki float ko'rinishidagi qiymatlarni butun songa o'zgartiradi.
# Bunda matn butun son ko'rinishida bo'lishi kerak.
# float()— matn yoki int ko'rinishidagi qiymatlarni o'nlik songa o'zgartiradi.
ism = 'Jobir'
yosh = 36
xabar = ism + ' ' + str(yosh) + ' yoshda'  # int ni string ga o'girish
print(xabar)
###
# O'ZGARUVCHI TURINI TEKSHIRISH
ism = 'Jobir'
yosh = 36
print(type(ism))  # ism degan o'zgaruvchining turini konsolga chiqaramiz
print(type(yosh))  # ismyosh degan o'zgaruvchining turini konsolga chiqaramiz
###
# 1 foydalanuvchining tug'ilgan yilini so'raymiz va qiymatni int ga aylantiramiz
t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
# 2 foydalanuvchi yoshini xisoblaymiz
yosh = datetime.now().year - t_yil  # datetime.now().year → hozirgi yilni olish
# 3 foydalanuvchi yoshini konsolga chiqaramiz
print(f"Siz {yosh} yoshda ekansiz")
###
# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
x = int(input("Istalgan son kiriting:\n>>>"))
print(x, " ning kvadrati ", x ** 2, " ga teng")
print(x, " ning kubi ", x ** 3, " ga teng")

# Foydalanuvchining yoshini so'rang,
# va uning tug'ilgan yilini hisoblab, konsolga chiqaring.
yosh = int(input("Yoshingiz nechida? \n>>>"))
t_yil = datetime.now().year - yosh
print("Siz ", t_yil, " da tug'ilgansiz")

# Foydalanuvchidan ikki son kiritshni so'rab,
# kiritilgan sonlarning yig'indisi, ayirmasi,
# ko'paytmasi va bo'linmasini chiqaruvchi dastur
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
print("a+b=", a + b)
print("a-b=", a - b)
print("axb=", a * b)
print("a/b=", a / b)
