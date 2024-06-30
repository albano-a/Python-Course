# import modulo.meu_modulo as mod
# from modulo.meu_modulo import saudacao

import math
from math import cos

raiz = math.sqrt(16)
seno = math.sin(2)
coss = cos(2)
# print(raiz)
# print(seno)
# print(coss)

import datetime

atual = datetime.datetime.now()
# print(atual)

data_especifica = datetime.datetime(2875, 6, 29, 12, 30, 45)
# print(data_especifica)

hoje = datetime.date.today()
# print(hoje)

amanha = hoje + datetime.timedelta(days=50)
# print(amanha)

dif = datetime.datetime(2024, 6, 29, 12, 00, 00) - datetime.datetime(
    1945, 5, 8, 12, 00, 00
)
# print(dif)

data_form = atual.strftime("%d/%m/%Y, %H:%M:%S")
# print(data_form)

data_string = "29/06/2024 10:30:00"
data_parseada = datetime.datetime.strptime(data_string, "%d/%m/%Y %H:%M:%S")
# print("Data parseada:", data_parseada)

import random

inteiro = random.randint(1, 30)
# print(inteiro)

import numpy as np

x = np.linspace(1, 10, 5)
print(x)
