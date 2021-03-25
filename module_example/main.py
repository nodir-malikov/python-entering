import module_example.avto_info_mod as aim  # Butun modulni dasturga ko'chirish
from math import pi, pow, sqrt  # modulning ayrim funksiyalarini ko'chirib olish
import random as r  # 'as' - import qilinayotgan modul nomini yoki funksiya nomini qisqartirishga yordam beradi.

# MODULDAN FAQAT FUNKSIYA EMAS, O'ZGARUVCHILAR HAM KO'CHIRIB OLSA BO'LADI

avto1 = aim.avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2020, 30000)
aim.info_print(avto1)

print()

print(pi)
print(pow(5, 2))
print(sqrt(5))

print()

print(r.randint(0, 100))

print()

ismlar = ['olim', 'anvar', 'hasan', 'husan']
ism = r.choice(ismlar)  # ismlar dan tasodifiy ism tanlaymiz
print(ism)
print(r.choice(ism))  # ismdan tasodifiy harf tanlaymiz

print()

x = list(range(0, 51, 5))
print(x)
print(r.choice(x))

print()

# shuffle(x) x ichidagi elementlarni tasodifiy tartibda qaytaruvchi funksiya. Bunda x bir necha elementdan iborat
# o'zgaruvchi (matn, ro'yxat) bo'lishi kerak.
x = list(range(11))
print(x)
r.shuffle(x)
print(x)
