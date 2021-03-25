class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil


class Talaba(Shaxs):  # Talaba klassi Shaxs klassidan vorislik oldi
    """Talaba klassi"""

    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)  # Super methodi orqali Shaxs klassidagi
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    # Polymorphism
    # BU YERDA SHAXS dagi get_info methodi OVERRIDE QILINMOQDA
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info


class Manzil:
    """Manzil saqlash uchun klass"""

    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil


# inson = Shaxs("Hasan", "Alimov", "FB001122", 1995)
# print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")
#
# print()

# talaba = Talaba("Valijon", "Aliyev", "FA112299", 2000, 'N00000011')
# print(talaba.get_info())

print()

talaba_manzil = Manzil(12, 'Olmazor', "Bog'bon", "Samarqand")  # talabaning manzilini yaratib olamiz
talaba = Talaba("Valijon", "Aliyev", "FA112299", 2000, "0000012", talaba_manzil)
# manzilni talabani yaratayotganda berib yuboramiz
print(talaba.manzil.get_manzil())
print(talaba.get_info())
print(f"{talaba.get_info()}. {talaba.get_age(2021)} yoshda.")
