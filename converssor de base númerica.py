import colorama
from colorama import Style, Back,Fore
colorama.init(autoreset=True)
num = int(input(f'{Back.BLACK+Fore.GREEN+Style.BRIGHT}Digite um número inteiro'))
print(f"""{Back.BLACK+Fore.BLUE+Style.BRIGHT}Escolha uma base para conversão:
1] converter para BINÀRIO
2] converter para OCTAL
3] converter para EXADECIMAL""")
opção= int(input(f'{Back.BLACK+Fore.GREEN}Sua opção:'))
if opção == 1:
   print(f'{Back.BLACK+Fore.GREEN}{num} BINÁRIO fica {bin(num)[2:]}')
elif opção== 2:
   print(f'{Back.BLACK+Fore.GREEN} {num} convertido para OCTAL fica{oct(num)[2:]}')
elif opção== 3:
    print(f'{Back.BLACK+Fore.GREEN}{num} convertido para EXADECIMAL fica {hex(num)[2:]}')
else:
    print(f'{Back.BLACK+Fore.RED}Opção invalida')

