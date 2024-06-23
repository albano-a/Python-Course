# Listas são estruturas de dados que armazenam valores.
# São sempre envoltas por [...]
jogo1 = "GTA"
jogo2 = "RDR"
jogo3 = "DS3"

# jogos1 = [jogo1, jogo2, jogo3]
#          0      1      2
#         -3      -2     -1
jogos = ["GTA", "RDR", "DS3"]
precos = [50, 50, 30]

# print(jogos2)
# valor1 = jogos[0]
# precos1 = precos[0]
# print("Os jogos são", jogos[0])
# print(precos1)

jogos.append("COD")
# print(jogos)
precos.append(10)
# print(precos)

notas = [7.9, 9.3, 8.2, 6.3, 7.2, 10.0]
notas1 = notas[1:5]  # sublista
# print(notas1)

altura = [1.75, 1.60, "não soube responder", 1.98]
altura_dob = altura * 2
# print(altura_dob)

lista1 = [1, 2, 3]
lista2 = [5, 6, 7]
# print(lista1 - lista2)
lista1[1] = 100
# print(lista1)
altura[2] = 1.88
# print(altura)
# print(1.75 not in altura)
