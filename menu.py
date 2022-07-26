#q q ta conte seno?
from time import sleep
encerrar = False
soma = 0
print('=-=--='*12)
primeiro_valor = int(input('Digite um valor: '))
mais_um_valor = int(input('Digite outro valor: '))
print('=-=--='*12)
while not encerrar:
    operacao =int(input('''Qual operação deseja  realizar com esses valores?
Digite a opção conforme a sua escolha:
[1] Para somar
[2] multiplicar
[3] Saber qual o maior numero
[4] novos números
[5] Encerrar operações
Informe aqui sua opção: '''))
    print('=-=--=' * 12)
    if operacao == 5:
        print("Finalizando operação... ")
        sleep(2)
        encerrar = True
    if operacao == 1:
        soma = primeiro_valor + mais_um_valor
        print(f'A soma desses valores é {soma}')
    if operacao == 2:
        soma = primeiro_valor * mais_um_valor
        print(f'A multiplicção de {primeiro_valor} e {mais_um_valor} é igual a {soma}')
    if operacao == 3:
        if primeiro_valor > mais_um_valor:
            print(f'O valor {primeiro_valor} é maior que {mais_um_valor}')
        elif primeiro_valor < mais_um_valor:
            print(f'O valor {mais_um_valor} é maior que {primeiro_valor}')
        else:
            print(f'Os dois valores são iguais.')
    if operacao == 4:
        primeiro_valor = int(input('Digite um valor: '))
        mais_um_valor = int(input('Digite outro valor: '))
        if operacao== 5:
            encerrar = True
        else:
            encerrar = False
    if operacao not in range(1, 6):
         sleep(1)
         print('Opção inválida')
    print('=-=--=' * 12)
    sleep(2)
