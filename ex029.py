'''
Exercicio 029
Escreva um programa que leia a velocidade de um carr.
Se ele ultrapassar 80Km/h. Mostre uma mensagem dizendo que ele foi multado.
A Multa vai custar R$7,00 para cada Km
'''

MULTA_POR_KM = 7

velocidade = int(input('Digite a velocidade em KM/H (apenas números): '))
if velocidade > 80:
    print(
        f'Você está acima da Velocidade permitida e foi multado em R$ {((velocidade-80)*MULTA_POR_KM):.2f}')
