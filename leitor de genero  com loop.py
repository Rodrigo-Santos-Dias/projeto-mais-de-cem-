
genero = str(input('Digite sua resposta de acordo com as opções [F] para feminino [M] para masculino: ')).title().strip()
while genero!= 'F' and 'M':
    print('Resposta invalida!!!')
    genero = str(input('Digite sua resposta de acordo com as opções [F] para feminino [M] para masculino: ')).title().strip()
    # if não necessario
if genero in 'MF':
    print(f'Okay genero {genero} validado')



