car_0 = {'model': 'ferrari', 'rang': 'qizil'}  # kalit so'z : javob
print(car_0['model'])
print(car_0['rang'])
###
en_uz = {
    'apple': 'olma',
    'apricot': 'o\'rik',
    'banana': 'banan'
}

print(en_uz)
print(en_uz['apple'])
print(en_uz['apricot'])
print(en_uz['banana'])
###
mevalar = {
    'olma': 10000,
    'tarvuz': 15000,
    'qovun': 12000
}
print(f"Olma narxi {mevalar['olma']} so'm")
###
talaba_0 = {
    'ism': 'nodir',
    'yosh': 17,
    't_yil': 2004
}
print(f"{talaba_0['ism'].title()}, {talaba_0['yosh']}-yoshda, {talaba_0['t_yil']}-tug'ilgan yili.")
###
# Yangi kalit so'z kiritish va qiymar qo'shish
talaba_0['kurs'] = 4
talaba_0['familiyasi'] = 'malikov'
print(talaba_0)
# Kalit so'z qiymatini o'zgartirish
talaba_0['ism'] = 'toxir'
print(talaba_0)

###
print()
# Bo'sh lug'at yaratish
talaba_1 = {}
print(talaba_1)
talaba_1['ism'] = 'bobur'
talaba_1['yosh'] = 18
talaba_1['kurs'] = 1
print(talaba_1)
print(f"Talaba: {talaba_1['ism'].title()}, {talaba_1['kurs']}-kurs")

###
print()
# Element ni o'chirish
del talaba_0['familiyasi']
print(talaba_0)
###
print()

# Agar lug'atda mavjud bo'lmasa
translate = en_uz.get('pinapple', 'Topa olmadim!')
print(translate)
# yoki
meva = mevalar.get('pinapple')
print(meva)
###
print()
### ITEMS()
talaba_0 = {
    'ism': 'alijon',
    'familiya': 'shamshiyev',
    'yosh': 22,
    'fakultet': 'matematika',
    'kurs': 4
}

print(talaba_0.items())
###
print()
###
for kalit, qiymat in talaba_0.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat} \n")
###
print()
###
telefonlar = {
    'ali': 'iphone x',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'orif': 'nokia 3310'
}

for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")
###
print()
### KEYS()
mahsulotlar = {  # Do'kondagi mahsulotlar
    'olma': 10000,
    'anor': 20000,
    'uzum': 40000,
    'anjir': 25000,
    'shaftoli': 30000
}

print(mahsulotlar.keys())
###
print()
### VALUES()
mahsulotlar = {  # Do'kondagi mahsulotlar
    'olma': 10000,
    'anor': 20000,
    'uzum': 40000,
    'anjir': 25000,
    'shaftoli': 30000
}

print(mahsulotlar.values())
###
print()
###
bozorlik = ['anor', 'uzum', 'non', 'baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
###
print()
###
#  LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH
print("Do'konimizdagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())
###
print()
###

#
telefonlar = {
    'ali': 'iphone x',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'orif': 'nokia 3310',
    'hamida': 'galaxy s9',
    'maryam': 'huawei p30',
    'tohir': 'iphone x',
    'umar': 'iphone x'
}

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)
# Yuoqirdagi natijaga e'tibor bersanigz, bir nechta foydalanuvchilar iphone x va galaxy s9 telefonidan foydalanishar
# ekan, va bu modellar qayta-qayta konsolga chiqdi. Buning oldini olish uchun set() funktsiyasidan foydalanishimiz
# mumkin.
print()
print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):
    print(tel)
# Pythonda set yana bir ma'lumot turi bo'lib, ro'yxat va lug'at kabi bir nechta elementlarni saqlashga mo'ljallangan.
# Lug'at va ro'yxatdan farqli ravishda, set ichidagi elementlar biror tartibda saqlanmaydi, va ularga indeks orqali
# murojat qilib bo'lmaydi. Shuningdek, set ichida bir hil elementlar bo'lmaydi.
