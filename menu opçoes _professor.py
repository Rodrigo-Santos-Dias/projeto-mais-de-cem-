from  time import sleep
n1 = int(input('primeiro valor: '))
n2 = int(input('Segundo valor : '))
opercao = 0
while opercao != 5:
    print('''[1]
    [2]
    [3]
    [4]
    [5]''')
    operacao = int(input('>>>sua opção>>>> '))
    if operacao == 1:
        soma = n1+n2
        print(f'A soma de {n1} com {n2} é igual á {soma}')
    elif operacao == 2:
        produto = n1 * n2
        print(f'A multiplicação de {n1} X {n2} é igual a {produto}')
    elif operacao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif operacao == 4:
        print(f'Informe novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif operacao == 5:
        print('Finalizando...')
        print('=-=-='*10)
        sleep(2)