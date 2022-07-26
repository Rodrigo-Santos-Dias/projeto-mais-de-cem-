for c in range(1, 6):
    print('Hello World!!')
print('FIM')
for c in range(0, 6):
    print('Hello World')
print('Fim')
for c in range(6, 0, -1):
    print(c)
from time import sleep
import turtle
for c in range(10, -1, -1):
    sleep(1)
    print(c,end='')
print('POOOOOWOWWWOWOWOWOWOWOWO')
for c in range(0, 51, 2):
    print(c, end='')
n = int(input(f'Digite um numero!'))
for c in range (0, n+1):
    print(c)
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c %3==0:
        cont= cont+1
        soma= soma+c
print(f'A soma de todo os {cont} valores é {soma}')
