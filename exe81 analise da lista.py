numeros = list()
cont = 0

while True:
    numeros.append(int(input('Valores: ')))
    cont+=1
    continuar = str(input('Continuar?[S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Continuar?[S/N]: ')).strip().upper()
    if continuar == 'N':
        break
numeros.sort(reverse=True)
print(f'A lista contem {cont} valores ')
print(f'A lista ordenada em forma decrescente fica assim {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista ')
else:
    print('O valor 5 não foi digitado')


