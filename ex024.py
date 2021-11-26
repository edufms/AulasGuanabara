'''
Exercicio 024 
Verificar se o nome da cidade começa com a palavra SANTO
'''

cidade = ' '
while len(cidade) != 0:
    cidade = input('Digite o nome de uma cidade: ').strip()

    if not cidade.upper().find('SANTO'):
        print('Cidade começa com SANTO')
    else:
        print('Cidade não começa com SANTO')

    print(cidade[:5].upper() == 'SANTO')
