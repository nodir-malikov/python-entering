# son = 1  # son ga 1 qiymatini beramiz
# while son <= 5:  # toki son 5 dan kichik yoki teng ekan...
#     print(son, end=' ')  # son ni konsolga chiqaramiz,
#     son += 1  # songa 1 qo'shamiz.
#
# ###
# print()
# ###
# # # Qiymat orqali
# # print("Kiritilgan sonni kvadratini qaytaruvchi dastur...")
# # savol = "Istalgan son kiriting "
# # savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# # qiymat = ''
# # while qiymat != 'exit':
# #     qiymat = input(savol)
# #     if qiymat != 'exit':
# #         print(float(qiymat) ** 2)
#
# # # Flag
# # print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# # savol = "Istalgan son kiriting "
# # savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# # ishora = True  # flag
# # while ishora:
# #     qiymat = input(savol)
# #     if qiymat == 'exit':
# #         ishora = False
# #     else:
# #         print(float(qiymat) ** 2)
#
# # Break orqali
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#
# while True:  # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break  # tsiklni to'xtatish
#     else:
#         print(float(qiymat) ** 2)
#
# # sonlar = list(range(1, 11))
# # for son in sonlar:
# #     if son == 5:  # son 5 ga teng bo'lsa kod to'xtaydi
# #         break
# #     print(f"{son} ning kvadrati {son ** 2} ga teng")
#
# ###
# print()
# ###
# # Qadam tashlab o'tish
# # Continue
# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:  # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         continue
#     print(f"{son} ning kvadrati {son ** 2} ga teng")
#
# print()
#
# son = 0
# while son < 10:
#     son += 1
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)  # juft sonlar
#
# ###
print()
print()
###
ismlar = []
#
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n = 1  # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob == 'ha':
#         n += 1
#         continue
#     else:
#         break
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)  # ism kalit, yosh qiymat
#
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False
#
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# Ro'yxatdan ro'yxatga ko'chirish
talabalar = ['hasan', 'husan', 'olim', 'botir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = baho
print(baholangan_talabalar)