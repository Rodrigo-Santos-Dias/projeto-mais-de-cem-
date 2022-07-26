import colorama
from colorama import Style, Fore, Back
colorama.init(autoreset=True)
print(f'{Back.BLACK+Fore.LIGHTBLUE_EX+Style.BRIGHT}Confederação nacional de natação!!')
idade = int(input(f'{Back.BLACK+Fore.LIGHTBLUE_EX+Style.BRIGHT}Informe sua idade para podermos definir sua categoria'))
if idade > 0 and idade < 10:
    print(f'{Back.BLACK+Fore.LIGHTBLUE_EX+Style.BRIGHT}{idade} Anos você  pertence a categoria {Back.BLACK+Fore.GREEN+Style.BRIGHT}MIRIM')
elif idade  >9  and idade < 15:
    print(f'{Back.BLACK+Fore.LIGHTBLUE_EX+Style.BRIGHT}{idade} Anos você pertence a categoria {Back.BLACK+Fore.WHITE+Style.BRIGHT}INFANTIL')
elif idade >14  and idade< 20:
    print(f'{Back.BLACK+Fore.LIGHTBLUE_EX+Style.BRIGHT}{idade} Anos você pertence a categoria {Back.BLACK+Fore.YELLOW+Style.BRIGHT}JUNIOR')
elif idade > 19 and idade < 27:
    print(f'{Back.BLACK+Fore.LIGHTBLUE_EX+Style.BRIGHT}{idade} Anos você pertence a categoria {Back.BLACK+Fore.LIGHTCYAN_EX+Style.BRIGHT}SENIOR')
elif idade>26 :
    print(f'{Back.BLACK+Fore.LIGHTBLUE_EX+Style.BRIGHT}{idade} Anos você pertence a categoria {Back.BLACK+Fore.RED+Style.BRIGHT} MASTER')
