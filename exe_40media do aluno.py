import colorama
from colorama import Back, Style, Fore
colorama.init(autoreset=True)
print(f'{Back.BLACK+Fore.BLUE+Style.DIM}Vamos analisar sua nota e descobrir se você foi aprovado')
n1 = float(input(f'{Back.BLACK+Fore.BLUE+Style.DIM}Digite a primeira nota'))
n2 = float(input(f'{Back.BLACK+Fore.BLUE+Style.DIM}Digite a segunda nota'))
media = (n1+n2)/2
if media < 5.0:
    print(f'{Back.BLACK+Fore.RED+Style.DIM}Sua media foi de {media} você foi reprovado')
elif media > 7.0:
    print(f'{Back.BLACK+Fore.GREEN+Style.DIM}Sua media foi de {media} você foi aprovado parabéns')
else:
    print(f'{Back.BLACK+Fore.YELLOW+Style.DIM}Sua media foi de {media} vai ter de ficar de recuperação')
