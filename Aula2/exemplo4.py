"""
Verificar se a idade inserida pode votar não.
"""

idade = int(input("Digite uma idade: "))

if idade >= 16:
    print("Pode votar")
else:
    print("Não pode votar")