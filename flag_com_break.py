num = 0
cont=0
soma = 0
print('Digite 999 para parar:')
while num != 999:
    cont+=1
    soma+=num
    num =int(input('Didgite um número: '))
    if num == 999:
        break
print(f'A soma dos {cont} numeros dígitados é igual a {soma}')
