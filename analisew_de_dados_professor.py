soma_idade = 0
media_idade = 0
homemvelho = 0
nomevelho = 0
totmulher20 = 0
for p in range (1, 5):
    print(f'-------{p}Pessoa-------')
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]: ')).strip()
    soma_idade+= idade
    if p == 1 and sexo in 'Mm':
        homemvelho = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > homemvelho:
        homemvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20+=1
media_idade = soma_idade / 4
print( f'total de mulheres com menos  de 20 anos é de {totmulher20}')
print(f' a media de idade do grupo {media_idade}')
print(f'homen mais vellho é {nomevelho} e tem {homemvelho}')
