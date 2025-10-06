"""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
"""
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print(f'Seu nome começa com {nome[0]} e termina com {nome[len(nome)-1]}')
