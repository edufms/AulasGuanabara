'''
Exercicio 033
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

while True:
    n1 = int(input('Digite o primeiro Número: '))
    n2 = int(input('Digite o segundo Número: '))
    n3 = int(input('Digite o terceiro Número: '))

    if n1 > n2 and n1 > n3:
        print('O primeiro número é o maior!')
        if n2 < n3:
            print('O segundo número é o menor!')
        else:
            print('O terceiro número é o menor!')
    elif n2 > n3:
        print('O Segundo número é o maior')
        if n1 < n3:
            print('O primeiro número é o menor!')
        else:
            print('O terceiro número é o menor!')
    else:
        print('O Terceiro número é o maior')
        if n2 < n1:
            print('O segundo número é o menor!')
        else:
            print('O primeiro número é o menor!')
