# Estruturas de controle
# if-else ; while ; for
# if, else, elif

####################################
# Estrutura Condicional Simples
####################################

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode entrar!")

print("Idade:", idade)

####################################
# Estrutura Condicional Composta
####################################

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode entrar!")
else:
    print("Você não pode entrar!")

print("Idade:", idade)

### OBS: Operadores de comparacao: and, or
# and - verifica se os dois são verdadeiros ou falsos
# or - verifica se pelo menos um deles é verdadeiro ou falso

####################################
# Estrutura Condicional Encadeada
####################################
# else if = elif

idade = int(input("Digite sua idade: "))

if idade >= 75:
    print("Você é muito velho!")
    if idade > 100:
        print("Você existe?")
    else:
        print("Sai daqui!")
elif idade >= 18:
    print("Você pode entrar!")
else:
    print("Você não pode entrar!")

print("Idade:", idade)
