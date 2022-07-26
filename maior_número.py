import colorama
from colorama import Back, Fore, Style
colorama.init()
n1 = int(input(f'{Back.BLACK+Fore.BLUE}Digite o primeiro número:'))
n2 = int(input('Digite o segundo  número:'))
n3 = int(input('Digite o terceiro número:'))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and  n3 <n2:
    menor = n3
maior = n1
if n2 < n1 and n2 < n3 :
    maior = n2
if n3> n1 and n3 > n2:
    maior = n3
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
