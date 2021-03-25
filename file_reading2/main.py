filename = 'data\\talabalar.txt'

# # Bu usul faqatgina ro'yxatni ekranga chiqazadi
# with open(filename) as file:
#     for line in file:
#         print(line)

# Bu usul esa har bir qatorni alohida element sifatida ro'yxatda saqlaydi
with open(filename) as file:  # faylni o'qiyapmiz
    talabalar = file.readlines()

print(talabalar)

talabalar = [talaba.rstrip() for talaba in talabalar]  # \n larni o'chirib tashlaymiz

print(talabalar)

###
print()
###

# Yangi faylga yozish
faylnomi = 'data\\new_file.txt'  # fayl mavjud bo'lmasa yaratadi, agar bo'lsa unda o'chirib tashlaydi
ism = 'Olimov Hasan'
tyil = 2004
with open(faylnomi, 'w') as fayl:  # 'w' - bu biz faylni yozish uchun ochmoqchi ekanligimizni anglatadi
    # 'w' - FAQATGINA YANGI FAYL UCHUN MO'LJALLANGAN!
    fayl.write(ism + '\n')  # \n qo'shilmasa hamma narsalar bir qatorga yoziladi
    fayl.write(str(tyil) + '\n')  # yozilayotgan ma'lumot faqat STRING bo'lishi kerak


# Eski faylga qo'shish
faylnomi = 'data\\new_file.txt'
ism = 'Husan Hasanov'
tyil = 2002
with open(faylnomi, 'a') as fayl:  # 'a' - bu 'append' biz faylga ma'lumot qo'shmoqchiligimiz uchun ochmoqchi
    # ekanligimizni anglatadi
    # fayl mavjud bo'lmasa yaratadi
    fayl.write(ism + '\n')
    fayl.write(str(tyil) + '\n')
