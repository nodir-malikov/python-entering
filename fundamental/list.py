# LIST
mevalar = ['olma', "o\'rik", 'shaftoli']
print(mevalar)  # ro'yxat
print(len(mevalar))  # ro'yxat uzunligi
###
narxlar = [100, 200, 300]
print(narxlar)
###
sonlar = ["bir", "ikki", 3]  # har qanday typedagi ma'lumot ro'yxatda saqlana oladi
print(sonlar)
###
print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])
###
print("Birinchi meva: ", mevalar[0].title())
print("Ikkinchi meva: ", mevalar[1].upper())
###
print(narxlar[1] + narxlar[2])
###
car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
print(car_models[-1])  # Listning eng oxirgi elementiga -1 bilan murojat qilamiz
### Elementni o'zgartirish
narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 13000  # 1-qiymatni 13000 ga o'zgartiramiz
narhlar[2] = 11000  # 3-qiymatni 11000 ga o'zgartiramiz
narhlar[3] = narhlar[3] + 2000  # 4-qiymatga 2000 qo'shamiz
print(narhlar)
### Yangi element oxiriga qo'shish
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append("tarvuz")  # mevalar ga tarvuz qo'shamiz
print(mevalar)

cars = []  # bo'sh ro'yxat yaratamiz
cars.append('Lacetti')  # ro'yxatga Lacetti mashinasini qo'shamiz
cars.append('Nexia 3')  # ro'yxatga Nexia 3 mashinasini qo'shamiz
cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
print(cars)
### Ro'yxatning istalgan joyiga yangi element qo'shish
cars = ['Lacetti', 'Nexia 3', 'Cobalt']
cars.insert(0, 'Malibu')  # 1-o'ringa yangi qiymat qo'shamiz
print(cars)

cars.insert(2, 'Damas')  # 3-o'ringa yangi qiymat qo'shamiz
print(cars)
###  Elementni o'chirish
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
del mevalar[1]  # 2-element (anjir) ni o'chirib tashlaymiz
print(mevalar)
###  Element qiymati bo'yichi o'chirish
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
mevalar.remove('shaftoli')  # Ro'yxatdan shaftolini o'chirdik
print(mevalar)
# .remove(qiymat) metodi ro'yxatda uchragan birinchi mos keluvchi qiymatni o'chiradi. Agar ro'yxatning ichida 2 va
# undan ko'p bir hil qiymatli elementlar bo'lsa, ulardan eng birinchisi o'chadi.
hayvonlar = ['it', '`mushu`k', 'sigir', 'qo\'y', 'quyon', 'mushuk']
hayvonlar.remove("mushuk")  # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
print(hayvonlar)
### Sug'urib olish, o'chirish emas
bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3)  # Ro'yxatdan banan ni sug'urib olamiz
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)
# Agar .pop() metodida indeks berilmasa, ro'yxatdan o'xirgi qiymat sug'urib olinadi.

###
# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', "G'ani"]
# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
print(f"{ismlar[2]} va {ismlar[3]} egizaklar")
print(ismlar[-1] + " g'ildirakni g'izillatib g'ildratti")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_678_000, 112.4]
print(sonlar)

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning
# qiymatini o'zgartiring, ba'zilarini esa almashtiring.
sonlar[0] = sonlar[0] + sonlar[-1]
sonlar[1] = -67.8
sonlar[4] = sonlar[4] + 37
del sonlar[5]
print(sonlar)

# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning,
# ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
t_shaxslar = ['Amir Temur', 'Imom Buxoriy', 'Napoleon']
z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']

# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
suhbat qilishni istar edim\n")

# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni
# kiriting.
friends = []
friends.append('John')
friends.append('Alex')
friends.append('Danny')
friends.append('Sobirjon')
friends.append('Vanya')
print(friends)

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
friends.remove('John')
friends.remove('Alex')
print(friends)

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.append('Hasan')
friends.insert(0, 'Husan')
friends.insert(2, 'Ivan')
print(friends)

# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan
# do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)

###
print()
print()
print()
###  Ro'yxatlarni tartiblash
cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()  # alifbo bo'yicha tartiblandi
print(cars)
# Diqqat! Tartiblashda katta harflar kichik harflardan avval kelishini hisobga oling. Agar matndagi so'zlarning bosh
# harfi katta-kichik aralash yozilgan bo'lsa, ularni bir ko'rinishga keltirib olish maqsadga muvofiq bo'ladi.
cars = ['Bmw', 'mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
cars.sort()
print(cars)
### Teskari tartiblash
cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort(reverse=True)
print(cars)

###  .sort() metodi ro'yxatni tartiblaydi. Ba'zida asl ro'yxat ichidagi elementlarning ketma-ketligini buzmagan holda
# ro'yxatni tartiblash talab qilinishi mumkin. Buning uchun sorted() funktsiyasidan foydalanamiz:
mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)
###
print(sorted(mehmonlar, reverse=True))
###
ages = [12, 98, 34, 65, 34, 76, 11]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))
### Ro'yxatni aylantirish
fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
fruits.reverse()
print(fruits)
### Ro'yxat uzunligi
fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
print("Elementlar soni:", len(fruits))  # len(fruits) ro'yxat uzunligini qaytaradi

### Sonlar orasidagi sonlar
sonlar = list(range(0, 10))
print(sonlar)
# Diqqat! E'tibor qiling range() funktsiyasi ikkinchi indeksdan bitta avval to'xtaydi.
###  range() yordamida qadamni ham berishimiz mumkin
juft_sonlar = list(range(0, 20, 2))  # 0 dan 20 gacha 2 qadam bilan
toq_sonlar = list(range(1, 20, 2))  # 1 dan 20 gacha 2 qadam bilan
print("Juft sonlar: ", juft_sonlar)
print("Toq sonlar: ", toq_sonlar)

###
narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narhlar)  # minimumini topish
qimmat = max(narhlar)  # maksimumini topish
jami = sum(narhlar)  # hammasini qo'shib chiqazish
print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

### Ro'yxatni kesish
cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
my_cars = cars[0:3]  # 0-indeskdan boshlab 3 ta element ajratib olamiz
print(my_cars)
# Diqqat! Python 2-indeksdan bitta avval to'xtaydi. Yuqoridagi misolda ham 0,1,2-elementlar ajratib olindi.
print(cars[2:5])  # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)
print(cars[:4])  # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
print(cars[2:])  # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

### RO'YXATDAN NUSXA OLISH
sonlar = [1, 2, 3, 4, 5]  # donlar degan ro'yxat yaratamiz
sonlar2 = sonlar  # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
sonlar2.append(6)  # sonlar2 ga 6 sonini qo'shamiz
sonlar2.append(7)  # sonlar2 ga 7 sonini qo'shamiz
print("Bu sonlar ro'yxati:", sonlar)
print("Bu sonlar2 ro'yxati:", sonlar2)
# Natija biz kutgandek bo'lmaydi, chunki biz nusxa olmadik, shunchaki 2 chi ro'yxatni birinchiga bog'lab qo'ydik
sonlar = [1, 2, 3, 4, 5]  # donlar degan ro'yxat yaratamiz
sonlar2 = sonlar[:]  # [:] ro'yxatni to'liq ko'chirib oladi
sonlar2.append(6)  # sonlar2 ga 6 sonini qo'shamiz
sonlar2.append(7)  # sonlar2 ga 7 sonini qo'shamiz
print("Bu sonlar ro'yxati:", sonlar)
print("Bu sonlar2 ro'yxati:", sonlar2)
# Endi biz kutgandek!

###
print()
###
# Barcha nexia elementlarni o'chirish
cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia']
while 'nexia' in cars:  # toki nexia cars ro'yxati ichida ekan...
    cars.remove('nexia')  # nexia ni ro'yxatdan olib tashla
print(cars)
