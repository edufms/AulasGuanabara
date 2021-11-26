import math
'''
Exercicio 035
Desenvolva um programa que leia o comprimento de três retas e diga
ao usuario se elas podem ou não formar um triângulo
'''

a = int(input('Digite o lado 1 do triangulo: '))
b = int(input('Digite o lado 2 do triangulo: '))
c = int(input('Digite o lado 3 do triangulo: '))

triangulo = False

if a > math.fabs(b-c) and a < (b+c):
    if b > math.fabs(a-c) and a < (a+c):
        if c > math.fabs(b-a) and c < (a+b):
            triangulo = True
            print('Esses valores podem formar um triangulo')
if not triangulo:
    print('Esses valores NÃO podem formar um triangulo')
