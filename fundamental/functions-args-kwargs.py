# def summa(*sonlar): # Hohlagancha parametr beriladi bu funksiyaga
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi


# Soddaroq varianti
def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return sum(sonlar)


# Agar funksiya bir nechta argument qabul qilsa, *args argument doim oxirida yoziladi:


def summa_2(x, y, *sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya. x va y majburiy."""
    return x + y + sum(sonlar)


# **kwargs — keyword arguments (kalit so'zli argumentlar)
def avto_info(kompaniya, model, **malumotlar):  # **malumotlar - bu **kwargs
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar


print(summa(1, 2))
print(summa(1, 2, 3, 4, 5))

print(summa_2(1, 2, 3, 4, 5))

avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)  # Ixtiyoriy rang va yil argumentlari kiritildi
avto2 = avto_info("Kia", "K5", narh=35000, rang='qizil', yil=2019)  # **kwargs xoxlagan tartibda
print(avto1)
print(avto2)
