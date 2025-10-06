"""
Desenvolva um programa que pergunte a distância
de uma viagem em Km. Calcule o preço da passagem.
cobrando R$0,50 por Km para viagens de até 200km
e R$0,45 para viagens mais longas.
"""
dis = int(input('Qual é a distância da viagem em Km?: '))
if dis < 200:
    preco = dis * 0.50
else:
    preco = dis * 0.45
print(f'O preço para sua viagem ficou {preco} R$')