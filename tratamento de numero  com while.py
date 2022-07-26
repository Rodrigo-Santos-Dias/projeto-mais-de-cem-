from time import sleep
encerrar = False
cont = 0
soma = 0
media= 0
maior = menor = 0
continuar = ''
while encerrar == False:
    cont +=1
    num = int(input('Digite um número: '))
    soma+=num
    continuar =str(input('\nQuer continuar?[S/N] ')).upper()
    if continuar not in 'S/N':
        print('Resposta invalida')
        sleep(1)
        continuar = str(input('\nQuer continuar?[S/N] ')).upper()
    if cont == 1:
        menor = maior = num
    else:
        if num>maior:
            maior = num
        if num < menor:
            menor = num
    if continuar == 'N':
        encerrar = True
        print('Fim.')
media = soma/cont
sleep(1)
print(f'A média dos {cont} números digitados foi {media}\nO maior numero digitado é de {maior}\nO menor foi {menor}')
#o pai é brabo 09/11/2021
#nem tanto 11/11/2021