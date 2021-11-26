'''
Exercicio 025 
Verificar se o nome tem a palavra SILVA

'''

nome = ' '
while len(nome) != 0:
    nome = input('Digite um nome: ')

    if(nome.upper().find('SILVA') != -1):
        print('Nome Contem Silva')
    else:
        print('Nome não contem Silva')

    print(f'Existe Silva no nome? {"SILVA" in nome.upper()} \n')
