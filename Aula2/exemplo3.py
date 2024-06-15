"""
Verifique se um numero é positivo, negativo, ou zero e
imprima a mensagem correspondente
"""

numero = float(input("Digite um valor: "))

if numero == 0:
    print("O número é zero")
elif numero > 0:
    print("O numero é positivo")
else:
    print("O numero é negativo")