def saudacao(nome):
    return f"Olá, {nome}!"


saudar = saudacao
# print(saudar("João"))

soma = lambda x, y: x + y
# print(soma(2, 2))


def aplicar(func, valor):
    return func(valor)


# print(aplicar(lambda x: x ** 2, 4))

# Map e Filter
numeros = [1, 2, 3, 4]
quadrados = map(lambda x: x**2, numeros)
# print(list(quadrados))

numeros = [1, 2, 3, 4]
pares = filter(lambda x: x % 2 == 0, numeros)
# print(list(pares))

# Funções Puras
def soma_pura(x, y):
    return x + y

a, b = 2, 2
print(soma_pura(a, b))

# Funções Impuras
contador = 0

def incrementar():
    global contador
    contador += 1
    return contador

print(incrementar()) # Modifica a variável global 'contador'

# Imutabilidade - Evita mudanças de estado
numeros = [1, 2, 3]
novos_numeros = [x * 2 for x in numeros]
print(novos_numeros)