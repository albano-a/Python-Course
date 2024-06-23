# Funções são blocos de comandos que facilitam
# a repetição de códigos

# numero = int(input("Digite um valor: "))


def par_impar(numero):
    if numero % 2 == 0:
        print(numero, "é par")
    else:
        print(numero, "é ímpar")

import random

for i in range(5):
    n = random.randint(1, 100)
    par_impar(n)

"""python
def nome_da_funcao(parametros):
    o codigo da funcao
    
    return alguma coisa
    
CHAMAR A FUNCAO
nome_da_funcao(argumentos)
"""