from random import randint
cpu = randint(0, 10)
#firula
#firula
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Palpite'))
    palpite+=1
    if jogador == cpu:
        acertou = True
    else:
        if jogador > cpu:
            print('Menos.. tente mais uma vez.')
        elif jogador < cpu:
            print('Maior tente mais uma vez.')
print(f'Acertou com {palpite} tentativas parabéns')
#nessa eu ja declaro a variavel acertou como falsa e (while) enquanto ela for falsa o jogador recebe a perguta (input) palpite depois faço as comparações  para sabr
# se (if) os palpites são,acima, abaixo ou igual ao numero gerado  no randint
