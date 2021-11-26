from datetime import date
'''
Exercicio 032
Faça um programa que leia um ano qualquer e mostre se ele é bissexto!
'''

while True:
    ano = int(input('Digite um ano (Digite 0 para usar o ano atual): '))
    if ano == 0:
        ano = date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O Ano de {ano} é bissexto!!')
    else:
        print(f'O Ano de {ano} não é bissexto!!')
