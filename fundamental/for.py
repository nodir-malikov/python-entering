mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, siz to'yga taklif qilindingiz!")
###
print()
###
for mehmon in mehmonlar:
    print(mehmon)

print(mehmonlar)
###
print()
###
sonlar = list(range(1, 11))
for son in sonlar:
    print(f"{son} ning kvadrati {son ** 2} ga teng")
###
print()
###
sonlar = list(range(1, 11))  # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
sonlar_kvadrati = []  # bo'sh ro'yxat yaratamiz
for son in sonlar:  # sonlar dagi har bir son uchun
    sonlar_kvadrati.append(son ** 2)  # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz

print(sonlar)
print(sonlar_kvadrati)
###
print()
###
dostlar = []
print("5 ta eng yaqin do'stingizni ismini kiriting...")
for i in range(5):
    dostlar.append(input(f"{i + 1} - do'stingizni ismini kiriting: "))
print(dostlar)
###
print()
###
# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing,
# va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for ism in ismlar:
    print(f"Assalom alaykum, {ism}. Sahifamizga xush kelibsiz!")

# Yuoqirdagi tsikl tugaganidan so'ng,
# ekranga "Kod n marta takrorlandi" degan xabar chiqaring
# (n o'rniga kod necha marta takrorlanganini yozing)
print(f"Kod {len(ismlar)} marta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing.
# Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
sonlar = list(range(11, 100, 2))
for son in sonlar:
    print(son ** 3)

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang,
# va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
kinolar = []
print("5 ta sevimli kinoingiz qaysilar?")
for k in range(5):
    kinolar.append(input(f"{k + 1}-kino:"))
print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan
# uchrashganini (suhbatlashganini) so'rang,
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n + 1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)
