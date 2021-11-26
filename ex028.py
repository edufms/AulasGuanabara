import random

'''
Exercicio 028 
Jogo de adivinhação
Usuáro deverá colocar um valor e verificar se foi o emesmo gerado pelo computador
'''

numero = 0
while numero != 1000:
    try:
        numero = int(input('Digite um número de 0 a 5: '))
        rand = random.randint(0, 5)
        if numero > 5 or numero < 0:
            raise Exception('Digite um número entre 0 e 5')
        if numero == rand:
            print('Você ganhou!!!!!!!!!!!!!!')
        else:
            print(f'Você perdeu! Eu escolhi {rand}')
    except ValueError:
        print('Digite um número válido!')
    except Exception as e:
        print(e)
