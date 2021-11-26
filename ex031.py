'''
Exercicio 31
Desenvolva um programa que pergunte a distância de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200Km
e R$0,45 para viagens mais longas
'''

viagem_km = float(input('Digite a distância da Viagem em Km: '))

if viagem_km > 200:
    print(f'Será cobrado R$ {viagem_km*0.45} por essa viagem de {viagem_km}')
else:
    print(f'Será cobrado R$ {viagem_km*0.5} por essa viagem de {viagem_km}')

''' Usando if simplificado
preco = viagem_km * 0.5 if viagem_km < 200 else viagem_km * 0.45
print(preco)
'''
