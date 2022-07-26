#numeros primos são numeros que são totalmente divisiveis por dois numeros, que são respctivamente  os numesros 1 e o porprio numeron =
c = 0
n = int(input(f'Digite um número para saber se ele é primo ou não: '))
for i in range(1, n+1):
    if n % i == 0:
        c+=1
if c==2:
    print(f'O {n} foi divido do apenas {c} vezes portanto  é primo')
else:
    print(f'O {n}  foi dividido {c} vezes portanto não é primo')

