"""
-----------------------
Ruido       Decibel
-----------------------
Trem 130 db
Cortador de Grama 106 db
Despertador 70 db
Sala silenciosa 40 db

Escreva um programa que receba um valor de volume
e retorne/printe o ruido atribuído. Se o volume
coincidir com um dos ruidos, printa o ruido. Se não
printe o intervalo.
"""

vol = int(input("Digite um volume: "))

if vol > 130:
    print("Eu vou ficar surdo!")
elif vol < 40:
    print("Eu não consigo ouvir nada!")
elif 40 < vol < 70:
    print("Esse valor está entre Sala Silenciosa e Despertador")
elif 70 < vol < 106:
    print("Esse valor está entre Despertador e Cortador de Grama")
elif 106 < vol < 130:
    print("Esse valor está entre um Despertador e um Trem")
elif vol == 40:
    print("Sala Silenciosa")
elif vol == 70:
    print("Despertador")
elif vol == 106:
    print("Cortador de Grama")
elif vol == 130:
    print("Martelo Pneumático")
else:
    print("Inválido")