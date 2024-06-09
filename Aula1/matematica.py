# +, -, *, /, //, **, %

valor1 = 20
valor2 = 50

soma = valor1 + valor2  # 70
subtracao = valor1 - valor2  # -30
multi = valor1 * valor2  # 1000
divisao = valor1 / valor2  # 0.4

# print(soma, subtracao, multi, divisao)

divisao_inteira = valor1 // valor2  # 0
potencia = 2**2  #
potencia1 = pow(2, 2)
resto = 10 % 2

# print(divisao_inteira, potencia, potencia1, resto)

# Area de um trapezio

base_menor = 6
base_maior = 10
altura = 3

area_trapezio = (base_maior + base_menor) * altura / 2
print(area_trapezio)

# Volume de uma esfera

raio = 5
pi = 3.14159

volume_circulo = (4 / 3) * pi * raio**3
print(volume_circulo)
# round()
arre = round(volume_circulo, 4)
print(arre)
# format - f-string
print(f"O volume eh {volume_circulo:.2f}")
