sexo = ''
continuar = ''
homens =0
pessoasmaior18 = 0
mulheres_mnos_20 =0
while True:
    try:
        idade = int(input('Idade: '))
        if idade>18:
            pessoasmaior18+=1
    except ValueError:
        print('Valor ìnvalido')
        continue
    sexo = str(input('Sexo: [M/F]')).upper().strip()
    if sexo == 'M':
        homens+=1
    if sexo == 'F':
        if idade<20:
            mulheres_mnos_20+=1
    while sexo not in 'MF':
            print('Tente novamente.')
            sexo = str(input('Sexo: [M/F]')).strip().upper()
    try:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    except ValueError:
        print('Dado invalido')
        while continuar not in 'S''N':
            print('Resposta invalida tente novamente.')
            continuar = str(input(' Quer continuar? '))
            continue
    if continuar == 'N':
            break
print(f'(a) quantidade pessoas com mais de 18 anos é de {pessoasmaior18}\n(b) O total de homens  cadastrados foi de {homens}\n(c) A quantidade de mulheres com menos de vinte anos é de {mulheres_mnos_20}')
