# Funcao recursiva


def fatorial(num=0):
    """O que funcao faz aqui"""
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)


print(fatorial(num=8))
