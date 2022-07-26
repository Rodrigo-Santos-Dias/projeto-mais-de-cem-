import random

import colorama
from colorama import Back, Fore, Style
num = random.randint(0, 5)

colorama.init(autoreset=True)
print(f'{Back.BLACK+Fore.GREEN}*'*100)
tentativa = int(input(f'{Back.BLACK+Fore.GREEN}Pensei em um numero inteiro de 0 á 5 você cosegue adivinhar qual?'))
if tentativa==num:
    print(f'{Back.BLACK+Fore.BLUE}Prarabéns você acertou!')
else:
    print(f'{Back.BLACK+Fore.RED}Você errou eu pensei no número {num}!')



