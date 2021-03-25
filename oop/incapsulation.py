from uuid import uuid4  # har bir avto ga unikal id berish uchun


class Avto:
    """Avtomobil klassi"""
    __num_avto = 0

    def __init__(self, make, model, rang, yil, narh, km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km  # '__' - bilan biz km ga tashqaridan murojat qilib bolmaydigan qilib qo'ydik
        self.__id = uuid4()
        Avto.__num_avto += 1

    @classmethod  # Class ga tegishli methodlarni @classmethod dekorator (annotatsiyasi) bilan yozamiz
    def get_num_avto(cls):  # cls - bu class
        """Avtomobillar sonini qaytaramiz"""
        return cls.__num_avto

    def get_km(self):
        """Avto yurgan kilometrini chiqazish"""
        return self.__km

    def get_id(self):
        """Avto id sini chiqazish"""
        return self.__id

    def add_km(self, km):
        """Avto ga km qo'shish chiqazish"""
        if km >= 0:
            self.__km += km
        else:
            print('Mashina km sini kamaytirib bo\'lmaydi!')


avto1 = Avto('GM', 'Malibu', 'qora', 2020, 30000, 1000)

print(f'{avto1.get_km()} km')
print(f'ID: {avto1.get_id()}')

avto1.add_km(100)
print(f'{avto1.get_km()} km')

print(f'Avtomobillar soni: {Avto.get_num_avto()}')
