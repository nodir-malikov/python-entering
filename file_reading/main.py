# # Tavsiya qilinmaydigan usul
# file = open('pi.txt')
# PI = file.read()
# print(PI)
# file.close()

# print(file)
# print(type(file))


# Tavsiya qilinadigan usul
with open('pi.txt') as file:
    pi = file.read()

print(pi)
print()

pi = pi.rstrip()  # Fayl oxiridagi bo'shliqni olibtashlaymiz
pi = pi.replace('\n', '')  # Yangi qatorlarni olib tashlaymiz
pi = float(pi)  # son ko'rinishiga o'tkazamiz
print(pi)
