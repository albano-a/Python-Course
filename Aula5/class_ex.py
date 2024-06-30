# Métodos são funções definidas dentro de uma classe.
# Elas podem acessar e modificar os atributos do objeto.

# Atributos e métodos de classe são compartilhados entre todas
# as instancias de classe.

# Herança permite criar novas classes que herdam atributos
# e métodos de outra classe

class Veículo:
    def __init__(self, marca):
        self.marca = marca
        
    def info(self):
        return f"Veículo da marca {self.marca}"
    
class Carro(Veículo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo
        
    def info(self):
        return f"Carro {self.modelo} da marca {self.marca}"
    
carro2 = Carro("Toyota", "Corolla")
print(carro2.info())