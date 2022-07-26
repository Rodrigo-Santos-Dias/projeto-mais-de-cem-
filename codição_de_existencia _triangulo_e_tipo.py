import colorama
from colorama import Back, Style, Fore
colorama.init(autoreset=True)
print(f'{Back.BLACK+Fore.GREEN}Dê a medida das retas para saber se é possível formar um triangulo!')
r1 = float(input(f'{Back.BLACK+Fore.BLUE}Primeira medida'))
r2 = float(input(f'{"{0}{1}".format(Fore.MAGENTA, Back.BLACK)}Segunda medida:'))
r3 = float(input(f'{Fore.YELLOW+Back.BLACK}Terceira medida'))
if r1 + r2 > r3 and r2 + r3 >r1 and r1 + r3 > r2:
    print(f'{Fore.GREEN+Back.BLACK+Style.BRIGHT}Sim,com essas três retas é possível formar um triangulo ' ,end='')
    if r1==r2==r3:
        print(f'{Back.BLACK+Fore.LIGHTBLUE_EX+Style.BRIGHT}EQULATERO!!!')
    elif r1!=r2!=r3!=r1:
        print(f'{Back.BLACK+Fore.MAGENTA+Style.BRIGHT}ESCALENO!!!')
    else:
        print(f'{Back.BLACK+Fore.LIGHTMAGENTA_EX+Style.BRIGHT}ISÓCELES')
else:
    print(f'{Back.BLACK+Fore.RED+Style.BRIGHT}Não é possível formar um triangulo com essas medidas')