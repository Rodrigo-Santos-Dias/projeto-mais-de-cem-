lista=list()
maior=menor=''
posmai= posmen=''
for v in range(0,5):
    lista.append(int(input(f'Digite o {v} valor: ')))
    if len(lista) == 1:
        maior = menor = lista[v]
    else:
        if lista[v]>maior:
            maior=lista[v]
        if lista[v]<menor:
            menor=lista[v]
print('=-'*25)
print(f'Os valores digitados foram {lista}')
print('=-'*25)
print(f'O maior valor digitado foi {maior} nas posiçõe',end=' ')
for p,m in enumerate(lista):
    if maior == m:
        print(f'{p}..',end='')
    else:
        print(f'..',end='')
print(f'\nO menor valor digitado foi {menor} nas posições ',end=' ')
for i,men in enumerate(lista):
    if menor == men:
        print(f'{i}..',end='')
    else:
        print(f'..',end='')
print('\nFim do programa')
print('=-'*25)
 #   posemen = lista.index(menor)
#  print(f'{posmen}')

