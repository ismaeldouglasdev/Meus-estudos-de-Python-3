"""
Desenvolva um programa que leia
o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triangulo.
"""
a1 = int(input('Insira a primeira reta: '))
b2 = int(input('Insira a segunda reta: '))
c3 = int(input('Insira a terceira reta: '))
if a1 + b2 > c3 and a1 + c3 > b2 and b2 + c3 > a1:
    print('Essas retas podem formar um triângulo!')
else:
    print('Essas retas não podem formar um triângulo.')
