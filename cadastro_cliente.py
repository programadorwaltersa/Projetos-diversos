class Cliente:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def mostrar_dados(self):
        print(self.nome)
        print(self.idade)
        print(self.cpf)

class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor


    def mostrar_dados(self):
        print(self.marca)
        print(self.modelo)
        print(self.cor)

cliente1 = Cliente("Andre", 40, 12345678900)
carro1 = Carro("Toyota", "Corolla", "Cinza")

cliente1.mostrar_dados()
carro1.mostrar_dados()

