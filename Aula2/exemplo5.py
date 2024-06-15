"""
Escreva um programa que pergunte ao usuário o valor de um
ano qualquer e verifique se o ano é bissexto ou não.

> Dica:  Lembre-se de que um ano bissexto é aquele que é 
divisível por 4, mas não por 100, a menos que também seja 
divisível por 400. Isso significa que anos como 2000 e 2400 
são bissextos, mas anos como 1900 e 2100 não são. 
Certifique-se de exibir uma mensagem indicando se o 
ano é bissexto ou não.
"""

ano = int(input("Digite um ano: "))

if ano % 400 == 0:
    print("É bissexto")
elif ano % 100 == 0:
    print("Não é bissexto")
elif ano % 4 == 0:
    print("É bissexto")
else:
    print("Não é bissexto")
