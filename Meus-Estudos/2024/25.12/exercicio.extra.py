frase = input('Escreva uma frase ou palavra: ')
vogais = 'AEIOUaeiou'
contador_vogais = 0
for letra in frase:
    if letra in vogais:
        contador_vogais += 1
print(f'Total de vogais: {contador_vogais}')
