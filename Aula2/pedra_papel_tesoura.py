import random

opcoes = ("pedra", "papel", "tesoura")
jogando = True

while jogando:
    jogador = None # reinicia o jogador
    computador = random.choice(opcoes)
    
    while jogador not in opcoes:
        jogador = input("Escolha uma opção (pedra, papel, tesoura): ")
        
    print(f"Jogador: {jogador}")
    print(f"Computador: {computador}")
    
    if jogador == computador:
        print("É empate!")
    elif jogador == "pedra" and computador == "tesoura":
        print("Você ganhou!")
    elif jogador == "papel" and computador == "pedra":
        print("Você ganhou!")
    elif jogador == "tesoura" and computador == "papel":
        print("Você ganhou!")
    else:
        print("Você perdeu!")
        
    jogar_novamente = input("Jogar novamente? (s/n): ").lower()
    if not jogar_novamente == "s":
        jogando = False
        
print("Obrigado por jogar!")
        