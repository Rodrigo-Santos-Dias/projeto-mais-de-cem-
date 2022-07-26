from datetime import date
import colorama
from colorama import Back, Style, Fore
colorama.init(autoreset=True)
atual = date.today().year
print(f'{Back.BLACK+Fore.YELLOW}Vamos analisar a sua idade para poder confirmar se esta na hora de se alistar')
nasc = int(input(f'{Back.BLACK+Fore.GREEN+Style.BRIGHT}Ano de nascimento:'))
idade = atual-nasc
faltam = 18 - idade
if idade < 18:
    em = 18 - idade
    print(f'{Back.BLACK+Fore.YELLOW+Style.BRIGHT}Você tem {idade} anos inda faltam {faltam} anos para você se alistar em {atual+ em}')
elif idade > 18:
    em = idade - 18
    print(f'{Back.BLACK+Fore.YELLOW+Style.BRIGHT}Você tem {idade} anos ja passou a data do seu alistamento em {atual-em}')
else:
    print(f'{Back.BLACK+Fore.YELLOW+Style.BRIGHT}{idade} Anos. Seu paìs precisa de você!!')