import re
from pprint import pprint

from regex.uzwords import words

word1 = "темир"
word2 = "томир"
word3 = "тулпор"

andoza = "^т...р$"  # RegEx

# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))

matches = []
for word in words:
    if re.match(andoza, word):
        matches.append(word)

print(matches)

###
print()
###
#################### Email topish ####################
matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'  # Email ni topish uchun RegEx
email = re.findall(andoza, matn)  # find all - hamma topilgan email larni listga joylaydi
print(email)

###
print()
###
#################### Password kuchliligini tekshirish ####################
# Kuchli parolni tekshirish
# Quyidagi andoza ham ihateregex.io sahifasidan olindi
andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg = "Yangi parol kiriting"
msg += '(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, '
msg += '1 ta son va 1 ta maxsus belgi boʻlishi kerak): '

while True:
    password = input(msg)
    if re.match(andoza, password):
        print("Maxfiy so'z qabul qilindi")
        break
    else:
        print("Maxfiy so'z talabga javob bermadi")
