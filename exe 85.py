valores = list()
impares = list()
pares = list()
for c in range(1,8):
    itens = int(input(f'Dogite o {c} valor:'))
    if itens % 2== 0:
        pares.append(itens)
        pares.sort()
        valores.append(pares[:])
    else:
        impares.append(itens)
        impares.sort()
        valores.append(impares[:])
print(f'Os valores pares são {pares} ')
print(f'Os valores ímpares são {impares}')
