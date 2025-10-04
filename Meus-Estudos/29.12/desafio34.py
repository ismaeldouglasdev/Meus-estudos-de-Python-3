"""
Escreva um programa que pergunte
o salário de um funcionário e calcule o valor
do seu aumento.

Para salários superiores a R$1.250,00 calcule
um aumento de 10%.

Para os inferiores ou iguais, o aumento
é de 15%.
"""
s = int(input('Qual é o seu salário? '))
if s > 1250:
    a = s + (s * 10/100)
else:
    a = s + (s * 15/100)
print(f'Parabéns! seu salário aumentou e agora é {a}')
