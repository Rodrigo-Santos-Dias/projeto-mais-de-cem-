lista_num = list()
num = ''
continuar = ''
while True:
    num = int(input(f'Digite um número: '))
    if num not in lista_num:
        lista_num.append(num)
        print(f'Valor adicionado com sucesso!!')
    else:
        print(f'O número {num} ja faz parte da lista não vou adiciona-lo ')
    continuar = str(input(f'Deseja continuar?[S/N]')).title().strip()
    while continuar not in 'SN':
            continuar = str(input(f'Deseja continuar?[S/N]')).title().strip()
    if continuar == "N":
        break
lista_num.sort()
print(f'Você digitou os valores {lista_num}')
