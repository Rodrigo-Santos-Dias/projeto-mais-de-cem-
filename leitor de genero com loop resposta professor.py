genero = str(input('Informe seu genero : [M/F] ')).strip().upper()[0]
while genero not in 'MmFf':
    genero = str(input(f'{genero}´Essee dado foi considerado  invalido.Por favor informe novamente:  ')).strip().upper()[0]
print(f'Genero {genero} registrado com sucesso')  