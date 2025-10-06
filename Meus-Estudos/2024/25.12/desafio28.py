"""
Escreva um programa que faça o computador 'pensar'
em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo
computador.

O programa deverá escrever na tela  se o usuario venceu
ou perdeu
"""
from random import randint
from time import sleep
n1 = randint(0,5)
print('-=-' * 20)
print('Adivinhe qual número entre 0 e 5 eu escolhi!')
print('-=-' * 20)
n2 = int(input('Eu acho que o número é: '))
print('Processando... ')
sleep(2)
if n2 == n1:
    print('Parabéns você acertou!')
else:
    print(f'Errou! haahahahah eu pensei no número {n1}')