numero = int(input('Digite um número: '))
c = numero
fat = 1
print(f'{numero}! = {numero} ',end='')
while c > 0:
    fat *=c
    c -= 1
    print(f'X {c} ' if c > 0 else '=',end='')
print(fat)