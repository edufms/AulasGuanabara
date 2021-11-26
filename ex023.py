numero = ''
while len(numero) > 4 or len(numero) == 0:
    try:
        numero = int(input('Digite um número de 0 a 9999: '))
        u = numero // 1 % 10
        d = numero // 10 % 10
        c = numero // 100 % 10
        m = numero // 1000 % 10
        numero = str(numero).zfill(4)

    except:
        if not isinstance(numero, int):
            print('Digite um número Válido!')
            numero = ''
            pass

print('Usando String')
print(f'Unidade: {numero[3]}')
print(f'Dezena: {numero[2]}')
print(f'Centena: {numero[1]}')
print(f'Milhar: {numero[0]} \n')

print('Usando Int')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
