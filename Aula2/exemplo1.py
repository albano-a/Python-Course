"""
Escreva um condicional que além de printar se o número é
divisível ou não, também printe o resto da divisão,
tanto para valores que são divisíveis, quanto para os
que não são.
"""

num = int(input("Digite um valor: "))
resto = num % 10

if resto == 0:
    print("Esse nº é divisível por 10")
    print("O resto da divisão é:", resto)
    
print("O resto da divisão é:", resto)