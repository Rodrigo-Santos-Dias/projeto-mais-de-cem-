cont =0
soma =0
num = int(input('Mais uma vez:'))
if num !=999:
    while num != 999:
        cont+=1
        soma+=num
        num = int(input('Mais uma vez:'))
print(f'A soma dos {cont} números digitados é igual a {soma} ')
