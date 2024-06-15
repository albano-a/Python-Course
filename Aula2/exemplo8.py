"""
Faça um programa que some todos os ímpares de 0 a 100000
"""

soma = 0

for i in range(1, 100000, 2):
    soma += i

print(soma)
