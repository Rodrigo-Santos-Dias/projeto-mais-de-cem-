from time import sleep
from random import randint
itens=['pedra', 'papel', 'tesoura']
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra 
[1] Papel
[2] Tesoura''')
jogador = int(input(f'Qual sua jogada?'))
print('JO')
sleep(2)
print('KEN')
sleep(2)
print('PÕ')
sleep(2)
print('-='*12)
print(f'''Computador jogou {computador}
Jogador jogou {jogador}''')
print('-='*12)
if computador == 0:
    if jogador == 0:
        print(f'Empate')
    elif jogador == 1:
        print(f'Jogador venceu!!!')
    elif jogador == 2:
        print(f' Computador venceu!!!')
    else:
        print(f'Opçâo inválida!!!')
elif computador == 1:
    if jogador == 1:
        print(f'Empate')
    elif jogador == 0:
        print(f'Computador venceu!!!')
    elif jogador == 2:
        print(f'Jogador venceu!!!')
    else:
        print(f'Opçâo inválida!!!')
elif computador == 2:
    if jogador == 2:
        print(f'Empate!!!')
    elif jogador == 0:
        print(f'Jogador venceu!!!')
    elif jogador == 1:
        print(f'Computador venceu!!!')
    else:
        print(f'Opçâo inválida!!!')
elif computador == 2:
    print(f'Computador venceu')



