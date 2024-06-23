# Você pode retornar vários items em uma função


def bhaskara(a, b, c):
    delta = b**2 - 4 * a * c
    x1 = (-b + (delta ** (1 / 2))) / (2 * a)
    x2 = (-b - (delta ** (1 / 2))) / (2 * a)

    return x1, x2

x1, x2 = bhaskara(1, 1, 4)
print(x1, x2)
