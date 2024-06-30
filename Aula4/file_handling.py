# open()

# Copy Path - C:\Users\Icarl\Documents\GitHub\Python-Course\Aula4\hello.txt
# Copy Relative Path - Aula4\hello.txt
# escape sequences - \n, \t

# Escrevendo um arquivo
with open('dados.txt', 'w', encoding='utf-8') as file:
    file.write("Primeira linha\n")
    file.write("Segunda linha\n")
    
# Lendo o arquivo
with open('dados.txt', 'r', encoding='utf-8') as file:
    for linha in file:
        print(linha.strip())

