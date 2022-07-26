import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print(Fore.RED+'Qualquer coisa vermelha')
print('Hello world')
print(Back.CYAN+'ciano')
print(Style.BRIGHT+'alguma coisa brilhante')
print((Fore.RED + Back.GREEN+ 'vermelho com fundo verde'))
print(Fore.RED + Back.BLACK+Style.BRIGHT+'Que coisa horrorosa')
print(f'{Back.RED+Style.DIM+Fore.BLACK}teste')

