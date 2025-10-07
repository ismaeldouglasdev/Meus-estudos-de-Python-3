"""
Associação: Crie duas classes, Pessoa e Carro.
Faça com que Pessoa possa possuir um ou mais objetos Carro,
mas sem que Pessoa seja responsável por criar os carros.
Demonstre que os carros podem existir independentemente.
"""
from classes import Pessoa, Carro

p1 = Pessoa('Julia', 25)
c1 = Carro('Sedan', 'Vermelho')
p1.possuir_carro(c1)
print(p1)
# Desafio em progresso ainda
