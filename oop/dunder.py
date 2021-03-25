from pprint import pprint


class Avto:
    __num_avto = 0
    """Avtomobil klassi"""

    def __init__(self, make, model, rang, yil, narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1

    def __eq__(self, other):  # object ni object ga teng bo'lishini tekshirishni yoqish uchun shu funksiya qo'shiladi
        return self.narh == other.narh

    def __lt__(self, other):  # kichik yoki kattalik ni tekshirishni yoqish uchun
        return self.narh < other.narh

    def __le__(self, other):  # kichik yoki barobar, kattalik yoki barobar ni tekshirishni yoqish uchun
        return self.narh <= other.narh

    def __repr__(self):  # Java dagi toString methodi analogi
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.rang} {self.make} {self.model}"


class AvtoSalon:
    """Avtosalon klassi"""

    def __init__(self, name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"

    def __getitem__(self, item):  # AvtoSalon ning avtolar ro'yxatiga index bo'yicha murojat qilishni yoqadi
        return self.avtolar[item]

    def __setitem__(self, key, value):  # AvtoSalon ning avtolar ro'yxatiga index bo'yicha qo'shishni yoqadi
        self.avtolar[key] = value

    def add_avto(self, *avtolar):
        for avto in avtolar:
            if isinstance(avto, Avto):  # agar avto Avto klassidan bo'lsa
                self.avtolar.append(avto)
            else:
                print("Avto obyketini kiriting")


salon1 = AvtoSalon('MaxAvto')

avto1 = Avto('GM', 'Matiz', 'Oq', 2020, 50000)
avto2 = Avto('UZ', 'Spark', 'Oq', 2020, 40000)
print(avto1)
pprint(dir(avto1))

print()

print(avto1 >= avto2)
print(avto1 == avto2)
print(avto1 < avto2)

salon1.add_avto(avto1, avto2)

print(salon1)
print(salon1[:])
print(salon1[0])

salon1[0] = avto2

print(salon1)
print(salon1[:])
print(salon1[0])
