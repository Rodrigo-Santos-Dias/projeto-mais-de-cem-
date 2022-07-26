import colorama
from colorama import Back,Style, Fore
colorama.init(autoreset=True)

from random import randint
from time import sleep
# imports feitos
itens =['pedra', 'papel', 'tesoura']
computador = randint(0,2)
print(f'{Fore.GREEN+Style.BRIGHT:^68}Vamos jogar JOKENPÔ')
jogador = int(input(f'''{Fore.LIGHTGREEN_EX+Style.BRIGHT:^68}
                                                               [0] Pedra
                                                               [1] Papel
                                                               [2] Tesoura
                                                             Qual a sua jogada?'''))
print(f'{Fore.LIGHTGREEN_EX+Style.BRIGHT:^68}JO')
sleep(1)
print(f'{Fore.LIGHTGREEN_EX+Style.BRIGHT:^68}KEN')
sleep(1)
print(f'{Fore.LIGHTGREEN_EX+Style.BRIGHT:^68}PÔ')
#comparaçâo
print(f'{Fore.RED+Style.BRIGHT:}-='*50)
print(f'{Fore.BLUE+Style.BRIGHT:^68}Computador jogou {itens[computador]}')
print(f'{Fore.YELLOW+Style.BRIGHT:^68}Jogador jogou {itens[jogador]}')
print(f'{Fore.RED+Style.BRIGHT}-='*50)
if computador == 0:
    if jogador == 0:
        print(f'{Fore.YELLOW+Style.BRIGHT:^68}EMPATE!!!')
    elif jogador == 1:
        print(f'{Fore.LIGHTBLACK_EX+Style.BRIGHT:^68}Jogador VENCEU!!!')
    elif jogador == 2:
        print(f'{Fore.RED+Style.BRIGHT:^68}Computador VENCEU!!!')
    else:
        print(f'{Fore.BLACK+Style.BRIGHT:^68}JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 1:
        print(f'{Fore.YELLOW + Style.BRIGHT:^68}EMPATE!!!')
    elif jogador == 2:
        print(f'{Fore.LIGHTBLACK_EX + Style.BRIGHT:^68}Jogador VENCEU!!!')
    elif jogador == 0:
        print(f'{Fore.RED + Style.BRIGHT:^68}Computador VENCEU!!!')
    else:
        print(f'{Fore.BLACK + Style.BRIGHT:^68}JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 2:
        print(f'{Fore.YELLOW + Style.BRIGHT:^68}EMPATE!!!')
    elif jogador == 0:
        print(f'{Fore.LIGHTBLACK_EX + Style.BRIGHT:^68}Jogador VENCEU!!!')
    elif jogador == 1:
        print(f'{Fore.RED + Style.BRIGHT:^68}Computador VENCEU!!!')
    else:
     print(f'{Fore.BLACK + Style.BRIGHT:^68}JOGADA INVÁLIDA')
else:
    print(f'{Fore.BLACK + Style.BRIGHT:^68}JOGADA INVÁLIDA')

print(f'{Fore.RED+Style.BRIGHT}-='*50)




