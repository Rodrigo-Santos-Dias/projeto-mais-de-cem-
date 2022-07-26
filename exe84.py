dados = list()
galera = list()
cont = ''
totalpessoas = 0
maior_peso = menor_peso = 0
listamaiorpeso = list()
listamenorpeso = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Seu peso. ')))
    cont = str(input('Continua? [S/N]')).strip().upper()
    totalpessoas += 1
    galera.append(dados[:])
    dados.clear()
    if cont not in 'SN':
        while cont not in 'S''N':
            cont = str(input('Continua? [S/N]')).strip().upper()
    if cont == 'N':
        break
    for cada in galera:
        if totalpessoas == 1:
            menor_peso = maior_peso = cada[1]
        else:
            if cada[1] > maior_peso:
                maior_peso = cada[1]
            if cada[1] < menor_peso:
                menor_peso = cada[1]
for qualquer in galera:
    if qualquer[1] == maior_peso:
            listamaiorpeso.append(qualquer[0])
    if qualquer [1] == menor_peso:
        listamenorpeso.append(qualquer[0])
print(f'{totalpessoas} foi o total de  pessoas cadastradas ')
print(f'O menor peso registrado foi {menor_peso}Kg peso de {listamenorpeso}')
print(f'O maior peso registrado foi {maior_peso}Kg peso de {listamaiorpeso}')


