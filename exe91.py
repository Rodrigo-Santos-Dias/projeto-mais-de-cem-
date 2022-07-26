from time import sleep
from random import randint
from operator import itemgetter
jogadas = dict()
for jogada in range(1,2):
   jogadas["1"] = randint(1, 6)
   jogadas["2"] = randint(1, 6)
   jogadas["3"] = randint(1, 6)
   jogadas["4"] = randint(1, 6)
   #rankig.append(jogadas.keys())
   for jogador, item in jogadas.items():
       print(f'O jogador {jogador} tirou ---> {item}')
       sleep(1)
ranking =list()
print('=-'*30)
ranking = sorted(jogadas.items(),key=itemgetter(1),reverse=True)
print(ranking)
for pos,pontos in enumerate(ranking):
    print(f'{pos+1}lugar {pontos[0]} tirando {pontos[1]}')

