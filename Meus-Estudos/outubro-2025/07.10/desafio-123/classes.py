class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.carro = None

    def possuir_carro(self, carro):
        self.carro = carro
        return self.carro


class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor
