import os
'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
ex: Ana Maria da Silva
Primeiro: Ana
Último: Silva
'''


nome = ' '

while len(nome) != 0:
    nome = input('Digite um nome: ')

    nome_separado = nome.split()
    if len(nome_separado) == 0:
        break
    print(f'Primeiro Nome: {nome_separado[0]}')
    print(f'Último Nome: {nome_separado[-1]}')

os.system('cls')
