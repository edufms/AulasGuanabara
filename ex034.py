'''
Exercicio 034
Escreva um programa que pergunte o salário de um funcionário e calcule o 
valor do seu aumento.

Para Salarios superiores a R$1250,00, calcule um aumento de 10% que
Para os inferiores ou igual, o aumento é de 15%
'''

while True:
    salario = float(input('Digite o Salário: '))
    if salario > 1250:
        print('-=-' * 20)
        print(f'O salario aumentou de R${salario} para R${salario*1.1:.2f}')
        print('-=-' * 20)
    else:
        print('-=-' * 20)
        print(f'O salario aumentou de R${salario} para R${salario*1.15:.2f}')
        print('-=-' * 20)
