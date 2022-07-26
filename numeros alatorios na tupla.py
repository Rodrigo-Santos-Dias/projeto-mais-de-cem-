from random import randint
menor_num = maior_num = 0
print('Os numeros sorteados foram:', end='')
for n in range(1,6):
    list_num = randint(0, 10)
    print(f' {list_num}', end='')
    if n == 1:
        maior_num = menor_num = list_num
    else:
        if list_num > maior_num:
            maior_num = list_num
        elif list_num < menor_num:
            menor_num = list_num
print(f'\nO maior nùmero sorteado foi {maior_num}\nO menor nùmero sorteado foi {menor_num}')




