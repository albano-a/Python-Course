# Funções podem ter vários parâmetros


def saudacao(nome, idade, cidade):
    return f"Olá {nome}! Você tem {idade} anos e mora em {cidade}"


variavel = saudacao("Arthur", 36, "Saint Denis")
print(variavel)
