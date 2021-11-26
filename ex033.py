'''
Exercicio 033
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''


def ValorMenor(a, b, c):
    menor = a
    if b < a and b < c:
        menor = b
    if c < a and c < b:
        menor = c
    return menor


def ValorMaior(a, b, c):
    maior = a
    if b > a and b > c:
        maior = b
    if c > a and c > b:
        maior = c
    return maior


while True:
    n1 = int(input('Digite o primeiro Número: '))
    n2 = int(input('Digite o segundo Número: '))
    n3 = int(input('Digite o terceiro Número: '))
    menor = ValorMenor(n1, n2, n3)
    maior = ValorMaior(n1, n2, n3)
    print(f'Maior: {maior}')
    print(f'Menor: {menor}')

    if n1 > n2 and n1 > n3:
        print(f'O primeiro número ({n1}) é o maior!')
        if n2 < n3:
            print(f'O segundo número ({n2}) é o menor!')
        else:
            print(f'O terceiro número ({n3}) é o menor!')
    elif n2 > n3:
        print(f'O Segundo número ({n2}) é o maior')
        if n1 < n3:
            print(f'O primeiro número ({n1}) é o menor!')
        else:
            print(f'O terceiro número ({n3}) é o menor!')
    else:
        print(f'O Terceiro número ({n3}) é o maior')
        if n2 < n1:
            print(f'O segundo número ({n2}) é o menor!')
        else:
            print(f'O primeiro número ({n1}) é o menor!')
