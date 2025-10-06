"""
Escreva um programa que leia a velocidade de umm carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multado.

A multa vai custar R$7,00 por cada km acima do limite.
"""
print('-=-' * 20)
print("Radar da Rodovia")
print('-=-' * 20)
v1 = float(input('Insira a velocidade do carro (km/h): '))
limite = 80
taxa = 7
if v1 > limite:
    excesso = v1 - limite
    multa = excesso * taxa
    print(f'Você foi multado, excedeu o limite de 80 km/h e a sua multa é de {multa:.2f}.')
else:
    print('Você não foi multado')
print('Tenha um bom dia! Dirija com segurança!')