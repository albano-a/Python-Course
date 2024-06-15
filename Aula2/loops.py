# Estruturas de Repetição

#######################
# FOR
#######################

# for i in range(1, 10):
#     print(i)

# Somatorio 1 ate 5, i. 1 + 2 + 3 + 4 + 5

# soma = 0
# for i in range(5 + 1):
#     soma = soma + i
#     print(soma)

# Iterar sobre listas
#           0         1         2           3        4
frutas = ["maçã", "banana", "laranja", "melancia", "uva"]
tamanho = len(frutas)  # length = tamanho
# print(tamanho)
idade = [10, 15, 12, 13, 16]
soma = sum(idade)  # soma
# print(soma)
notas = [10.2, 154.3, 14.2]
maximo = max(notas)  # maximo dos valores de uma lista
minimo = min(notas)  # minimo dos valores de uma lista
# print(maximo, minimo)

# for fruta in frutas:
#     print(fruta)

# for number in range(0, 10, 2):
#     print(number)

palavra = "Python"  # ["P", "y" ...]
# for letra in palavra:
#    print(letra)
# print(palavra[1])

####################
# WHILE
####################

"""
while <condicao>:
    # bloco a ser executado
"""

# contador = 10

# while contador > 0:
#     print("Contador:", contador)
#     contador -= 1

number = int(input("Digite um número: "))
soma = 0

while number != 0:
    soma += number
    number -= 1

print(soma)
