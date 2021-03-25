### TUPLES - O'ZGARMAS RO'YXAT
tomonlar = (20, 30, 55.2)
print(tomonlar)
###
toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])

###
# toys = ('bus','car','bear','dino','snake','lizard')
# toys[3] = 'dragon'
# Natija: TypeError: 'tuple' object does not support item assignment
###

print()

# ## Agar Tuple ga o'zgartirish talab qilinsa, yagona yo'li o'zgarmas ro'yxatni list() funktsiyasi yordamida List (
# oddiy ro'yxat) ko'rinishiga keltirib olish, o'zgarishlarni bajarsih va qaytarib tuple() funktsiyasi yordamida
# o'zgarmas ro'yxatga o'tkazish mumkin:
toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')  # o'zgarmas ro'yxat
toys = list(toys)  # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# Ro'yxatga o'zgartirishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys)  # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
print(toys)
