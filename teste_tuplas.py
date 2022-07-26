lista = ('teu pai','tua prima','meu pai','minha prima')
#for cont in range(0,len(lista)):
    #print(lista[cont],cont+1)
    #resposta times brasileirâo
for pos, c in enumerate(lista):
    print(c, pos+1)
from random import sample

numeros = tuple(sample(range(0,11),5))
print(f'{numeros[0]}')
print(numeros)
