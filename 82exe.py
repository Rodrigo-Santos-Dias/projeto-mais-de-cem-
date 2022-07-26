lista_1= list()
continuar = ''
lista_par =list()
lista_impar=list()
while True:
    lista_1.append(int(input('Digite um valor: ')))
    continuar = str(input('Desja continuar? [N/S]')).strip().upper()
    if continuar not in 'S''N':
        while continuar not in 'S''N ':
            continuar = str(input('Desja continuar? [N/S]')).strip().upper()
    if continuar == 'N':
        break
for num in range(0, len(lista_1)):
    if lista_1[num] % 2 == 0:
        lista_par.append(lista_1[num])
    else:
        lista_impar.append(lista_1[num])
print('-='*20)
print(f'Essa é a sua lista completa {lista_1}')
print(f'Essa é a sua lista de números impares {lista_par}')
print(f'Essa é a sua lista de números pares {lista_impar}')


