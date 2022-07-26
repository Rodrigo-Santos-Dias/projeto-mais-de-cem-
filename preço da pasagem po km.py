import colorama
from colorama import Back, Style, Fore
colorama.init(autoreset=True)
km = int(input(f'{Back.WHITE+ Fore.BLACK+Style.BRIGHT}Qual a distancia dessa viagem?'))
if km<=200:
    print(f'{Back.WHITE+Fore.BLACK+Style.BRIGHT}A passaagem custará R${km*0.50 :.2f}')
else:
    print(f'{Back.WHITE+Fore.BLACK+Style.BRIGHT}A passagem custará R${km*0.45:.2f}')
print(f'{Back.WHITE+Fore.BLUE+Style.BRIGHT}Boa viagem')
