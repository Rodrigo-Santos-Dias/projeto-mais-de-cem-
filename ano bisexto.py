import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)
ano = int(input(f'{Back.BLACK+Fore.GREEN}Sobre qual ano voçê quer saber?'))
ano_b = ano%4
if ano_b == 0:
    print(f'{Back.BLACK+Fore.GREEN}O ano de {ano} é um ano bisexto')
else:
    print((f'{Back.BLACK+Fore.RED}O ano de {ano} não é um ano bisexto'))
