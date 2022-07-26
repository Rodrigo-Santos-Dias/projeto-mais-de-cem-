lista = [[], [], []]
pares =soma_terceira_coluna= maiorsegundacoluna=0
for c in range (0, 3):
    lista[c].append(int(input(f'Digite um valor para [{c},0]: ')))
    lista[c].append(int(input(f'Digite um valor para [{c},1]: ')))
    lista[c].append(int(input(f'Digite um valor para [{c},2]: ')))
print('-='*32)
for d in lista:
    for item in d:
        print(f'[{item:^5}]', end=' ')
        if item % 2==0:
            pares += item
    soma_terceira_coluna+=d[2]
    print()
print(f'A soma de todos os valores pares digitados: {pares}')
print(f'A soma dos valors da terceira coluna: {soma_terceira_coluna}')
lista[2].sort()
maiorsegundacoluna= max(lista[1])
print(f'O maior valor da segunda linha: {maiorsegundacoluna}')


