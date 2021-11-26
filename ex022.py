nome = str(input("Digite o seu nome completo:")).strip()

print(f'Seu nome em maísculo é: {nome.upper()}')

print(f'Seu nome em minusculo é: {nome.lower()}')

print(f"Com Split: {len(''.join(nome.split()))}")

print(f"Com Replace: {len(nome.replace(' ', ''))}")

print(f'Com count: {len(nome) - nome.count(" ")}')

print(
    f'Seu primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras')

print(f'Seu primeiro nome tem {nome.find(" ")} letras')
