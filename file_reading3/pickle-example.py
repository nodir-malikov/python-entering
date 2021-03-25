import pickle

# o'zgaruvchilarni faylga saqlab qo'yish uchun pickle ni ishlatamiz

# talaba1 = {'ism': 'hasan', 'familiya': 'husanov', 'tyil': 2000, 'kurs': 2}
# talaba2 = {'ism': 'husan', 'familiya': 'hasanov', 'tyil': 2001, 'kurs': 3}
#
# with open('info.pickle', 'wb') as file:  # wb - write binary degani, ya'ni binar shaklda yozamiz
#     pickle.dump(talaba1, file)  # dump - yozish
#     pickle.dump(talaba2, file)

# Aslida bu tavsiya qilinmaydi. Iloji boricha har bir o'zgaruvchuni alohida faylda saqlagan ma'qul
###########################################

# pickle yordamida o'zgaruvchilarni o'qish
with open('info.pickle', 'rb') as file:  # rb - read binary
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)

print(type(talaba1))
print(type(talaba2))
print(talaba1)
print(talaba2)
