from random import  randint
from time import sleep
numeros = list()
def sorteia(lista):
    print('Sorteando os numeros...',end='')
    for i in range(1,7):
        num = randint(1,10)
        lista.append(num)
        print(num,end=' ')
        sleep(1)
    print('Feito')


sorteia(numeros)
def soma_par(lista):
    pares = 0
    print(f'A soma dos pares de {lista} é' , end=' ')
    for n in numeros:
        if n %2 == 0:
            pares+= n
    print(pares)


soma_par(numeros)
