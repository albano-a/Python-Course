# Classes
# Programação Orientada a Objetos é um paradigma que
# utiliza objetos para modelar dados e comportamentos


# Uma classe define a estrutura e o comportamento de seus objetos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."


# Criar objeto
# Crie instâncias de classes para usar os dados e métodos definidos
pessoa1 = Pessoa("André", 24)
print(pessoa1.apresentar())

# Atributos de instância são dados únicos para cada objeto
pessoa2 = Pessoa("Daniel", 20)
print(pessoa2.nome)
print(pessoa2.idade)
