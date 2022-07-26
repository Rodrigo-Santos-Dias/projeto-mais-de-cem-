import colorama
from colorama import Back, Fore
colorama.init(autoreset=True)
salario = float(input(f'{Back.LIGHTBLACK_EX+Fore.LIGHTYELLOW_EX}Digite o seu salário para descobrir quanto terá de aumento!'))
if salario>1250:
    novo_salario =(10 * salario / 100) + salario
    print(f'{Back.BLACK + Fore.RED}O seu novo salário será deR${novo_salario:.2f}')
else:
    novo_salario=(15*salario/100)+salario
    print(f'{Back.BLACK+Fore.RED}O seu novo salário será deR${novo_salario:.2f}')


