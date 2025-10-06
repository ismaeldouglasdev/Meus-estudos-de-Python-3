"""
faça um programa que leia três
números e mostre qual é o maior
e qual é o menor.
"""
n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))
n3 = int(input('Insira o terceiro numero: '))
if n1 > n2 and n3:
    print(f'O número {n1} é o maior')
    if n2 > n3:
        print(f'e o número {n3} é o menor.')
    else:
        print(f'O número {n2} é o menor.')
else:
    if n2 > n3:
        print(f'O maior número é o {n2} e o menor é o {n1}')
    else:
        print(f'O maior número é o {n3} e o menor é o {n1}')

