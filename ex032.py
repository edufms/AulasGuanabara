'''
Exercicio 032
Faça um programa que leia um ano qualquer e mostre se ele é bissexto!
'''

while True:
    ano = int(input('Digite um ano: '))
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O Ano de {ano} é bissexto!!')
        else:
            print(f'O Ano de {ano} não é bissexto!!')
    elif ano % 4 == 0:
        print(f'O Ano de {ano} é bissexto!!')
    else:
        print(f'O Ano de {ano} não é bissexto!!')
