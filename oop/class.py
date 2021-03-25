# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#
#     def __init__(self, ism, familiya, t_yil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.t_yil = t_yil
#
#     def tanishtir(self):
#         """Talabani tanishtiradi qaytaradi"""
#         return f"Ismim: {self.ism} {self.familiya}, tug'ilgan yilim {self.t_yil}"
#
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
#
#     def get_surname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
#
#     def get_fullname(self):
#         """Talabaning ism va familiyasini qaytaradi"""
#         return f"{self.familiya} {self.ism}"
#
#     def get_age(self, yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil - self.t_yil
#
#     # Pythonda hech qanday vazifani bajarmaydigan pass operatori mavjud.
#     def describe(self):
#         pass
#
#     def get_email(self):
#         pass
#     # pass operatoridan if-else, for, while operatorlari badanida ham foydalanish mumkin


class Talaba:
    """Talaba nomli klass yaratamiz"""

    def __init__(self, ism, familiya, tyil):  # __init__ - bu konstruktor degandek gap
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "

    def set_bosqich(self, yangi_bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = yangi_bosqich

    def update_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1


class Fan():
    """Fan nomli klass"""

    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)  # talabalar ro'yxatiga qo'shiladi
        self.talabalar_soni += 1  # har bir yangi talaba qo'shilganda talabalar soni 1 taga oshadi

    def get_students(self):
        """Talabalar ro'yxatini chiqarish"""
        return [talaba.get_info() for talaba in self.talabalar]  # bir qator bilan for shakillantirish


# talaba1 = Talaba('Olim', 'Olimov', 2000)
# talaba2 = Talaba('Hasan', 'Husanov', 2004)
# talaba3 = Talaba('Botir', 'Karimov', 2008)
#
# print(talaba1.get_fullname())
# print(talaba1.get_age(2021))

talaba1 = Talaba("Alijon", "Valiyev", 2000)
print(talaba1.get_info())

talaba1.update_bosqich()  # 1 bosqichga oshiramiz
print(talaba1.get_info())

###
print()
###
talaba2 = Talaba("Akrom", "Ketmonov", 2002)

matem = Fan('Oliy matematika')

print(matem.nomi)
print(matem.talabalar)
print(matem.talabalar_soni)

matem.add_student(talaba1)  # talaba qo'shdik
matem.add_student(talaba2)

print(matem.talabalar)
print(matem.talabalar_soni)
print(matem.get_students())


########################## Klass ni ichidagi barcha biz yaratgan funksiyalarni qaytaradi
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]


##########################

print(see_methods(Talaba))

# __dict__ METODI Yuqorida zikr qilingan dunder metodlardan biri bu __dict__ metodi bo'lib, bu metod obyketning
# xususiyatlarini lug'at ko'rinishida qaytaradi:
print(talaba1.__dict__)
