from random import randint
vitorias = 0
print(f'Vamos jogar par ou ímpar')
while True:
    jogador = int(input('digite um numero de 0 a 10: '))
    while jogador>10:
        if jogador >10:
            print('jogue apenas numeros de 0 á 10:')
            jogador = int(input('digite um numero de 0 a 10: '))
    opcaojogador = str(input('Escolha par ou ímapar[P/I]')).strip().upper()
    while opcaojogador not in 'I''P':
        print('Jogue uma opção válida:[P/i]')
        opcaojogador = str(input('Escolha par ou ímapar[P/I]')).strip().upper()
    computador = randint(0, 10)
    soma=computador+jogador
    if (jogador+computador) % 2==0:
        if opcaojogador == 'P':
            vitorias += 1
            print(f'Eu joguei {computador} você jogou {jogador}.O total é {soma} um número  você ganhou')
        if opcaojogador == 'I':
            print(f'Eu joguei {computador} você jogou {jogador}.O total é  {soma} um número par você perdeu')
            break
    if (soma)%2!=0:
        if opcaojogador == 'I':
            vitorias += 1
            print(f'Eu joguei {computador} você jogou {jogador}.O total é  {soma}  um número  ìmpar você ganhou')
        if opcaojogador == 'P':
            print(f'Eu joguei {computador} você jogou {jogador}.O total é  {soma} um número ìmpar você perdeu')
            break
print(f'O total de vezes que você venceu foi {vitorias}')


