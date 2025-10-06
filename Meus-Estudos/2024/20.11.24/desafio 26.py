"""
Faça um programa que leia uma frase pelo teclado
e mostre:
> Quantas vezes aparece a letra "A"
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
"""
frase = str(input('Escreva uma frase: ')).upper().strip()
print("A quantidade de A's na frase é {}"
      .format((frase.count('A'))))
print("O primeiro 'A' aparece na {}° posição "
      .format((frase.find('A')+1)))
print("O último A na frase aparece na {}° posição."
      .format((frase.rfind('A')+1)))
