mi = 0
ihmv = 0
nhmv = 0
mmv = 0
sid = 0
for p in range (1, 5):
    n = str(input(f'Qual seu nome? ')).strip().title()
    idade = int(input(f'{n} Qual sua idade: '))
    genero = int(input(f'''{n} Selecione a opção de acordo com seu genero 
[1] Para feminino
[2] Para masculino
Informe aqui: '''))
    sid += idade
    mi = sid / p
    if genero == 2:
        if idade > ihmv:
            ihmv = idade
            nhmv = n
    if genero == 1:
        if idade < 20:
            mmv += 1
print(f'O homem mais velho se chama {nhmv} com {ihmv} anos')
print(f'Quantidade de mulheres com menos de vinte anos no grupo é {mmv}')
print(f'Media de idade do grupo é de {mi:.2f} anos')



