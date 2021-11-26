'''
Contar quantas letras a tem na frase
Onde a letra A aparece primeiro
Onde a letra A aparece por ultimo
'''

import os

frase = ' '
while len(frase) != 0:
    frase = input('Digite uma frase: ').strip()
    direita = frase.upper().rfind('A') + 1
    esquerda = frase.upper().find('A') + 1
    cont = frase.upper().count('A')
    #cont = 0

    # for i in range(len(frase)):
    #    if frase[i].upper() == 'A':
    #        cont += 1

    print(f'Esquerda: {esquerda}')
    print(f'Direita: {direita}')
    print(f'Possui {cont} letras "A"')

os.system("cls")
