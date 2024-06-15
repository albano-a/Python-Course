"""
Crie um programa que peça para o usuário digitar uma senha
e se a senha estiver errada, perguntar novamente.
"""

pwd = ""

while pwd != "123":
    pwd = input("Senha: ")
    if pwd != "123":
        print("Senha incorreta!")

print("Acesso Liberado!")
