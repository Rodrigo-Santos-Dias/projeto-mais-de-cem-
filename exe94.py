galera = dict()
dados = list()
mulheres = list()
p = mediaidade = somaidade= 0
cont = ''
pesoasacimadamedia= list()
while True:
    galera["nome"]=str(input(('Nome: '))).strip().title()
    galera["sexo"]=str(input(('Sexo [M/F]:'))).strip().upper()
    if galera["sexo"] not in "MmFf":
        while galera["sexo"] not in "MmFf":
            print('Dado inválido tente novamente [M/F]')
            galera["sexo"] = str(input(('Sexo [M/F]:')))
    galera["idade"]=int(input(('Idade: ')))
    p+=1
    dados.append(galera.copy())
    cont = str(input('continuar? ')).strip().title()
    if cont not in "Nn"'Ss':
        while cont not in "Nn"'Ss':
            print('Resposta invalida, responda com S ou N ')
            cont = str(input('continuar? ')).strip().title()
    if cont in 'N''n':
        break
for c,v in enumerate(dados):
    somaidade += dados[c]["idade"]
    if dados[c]["sexo"] == 'F':
        mulheres.append(dados[c]["nome"])
mediaidade = somaidade/p
for pos , i in enumerate(dados):
    if dados[pos]["idade"]> mediaidade:
         pesoasacimadamedia.append(dados[pos].copy())
print('=-'*30)
print(f'O grupo tem  {p} pessoas')
print('A  mulheres cadastradas foram ', end=' ')
for m in mulheres:
    print(f' {m}',end=' ')
print()
print('=-'*30)
print('Lista das pessoas que estão acima da media')
for i,y in enumerate(pesoasacimadamedia):
    for k,v in y.items():
        print(f'{k} = {v};',end='')
    print()
print(f'Media de idade é de  {mediaidade:.1f} anos')
print('=-'*30)


