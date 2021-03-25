###
ism = "Ahad"
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"  # f-string → matnlarni inkapsulyatsiyasiz qo'llash
print(ism_sharif)
###
ism = "James"
familiya = 'Bond'
print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")
###
print('Hello World!')  # Oddiy tekst
print('Hello \tWorld!')  # Joy tashlash
print('Hello\nWorld!')  # Keyingi qatorga o'tish
###
print(ism_sharif.upper())  # Hamma harflarni katta harf qilib yozadi
###
print(ism_sharif.lower())  # Hamma harflarni kichkina harf qilib yozadi
###
ism_sharif = 'james bond'
print(ism_sharif.title())  # Har bir so'zning birinchi harfini kattadan yozadi
###
ism_sharif = 'james bond'
print(ism_sharif.capitalize())  # Matndagi birinchi harfni katta harfdan yozadi
###
# lstrip() — matn boshidagi bo'shliqni,
# rstrip() – matn oxiridagi bo'shliqni,
# strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi
meva = "     olma     "
print("Men " + meva + " yaxshi ko'raman")
print("Men " + meva.lstrip() + " yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() + " yaxshi ko'raman")
###
# ism = input("\nIsmingiz nima?\n>>>")  # Java dagi Scanner, Pythonda input methodi
# print(f"Assalomu alaykum, {ism.title()}!")
###
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
print(f"{kocha}, {mahalla}, {tuman}, {viloyat}")
