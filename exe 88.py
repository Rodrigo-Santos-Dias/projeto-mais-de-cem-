from random import randint
from time import sleep
print('JOGA NA MEGA SENA')
quantjogos = int(input('Quantos jogos quer sortear ? '))
palpites= list()
for j in range(0,quantjogos):
    palpites.append(list())
    for n in range(0,6):
        palpites[j].append(randint(0, 60))
        while palpites[j].count(palpites[j][n]) > 1:
            palpites[j][n] = randint(0, 60)
    palpites[j].sort()
    print(palpites[j])
    sleep(1)
print()