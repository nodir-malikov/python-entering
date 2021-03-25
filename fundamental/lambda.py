# lambda YOHUD NOMSIZ FUNKSIYA

# lambda argument:ifoda

import math

uzunlik = lambda pi, r: 2 * pi * r  # r - bu radius
print(uzunlik(math.pi, 10))

print()

product = lambda x, y: x ** y
print(product(3, 2))

print()


def daraja(n):
    return lambda x: x ** n


kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")
