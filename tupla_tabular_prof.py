palavra = ('Sua Prima', 2.50, 'Seu Pai', 3.95,'Minha Prima',500, 'Meu Pai',100)
for p in range (0,len(palavra)):
    if p % 2 == 0:
        print(f'{palavra[p]:.<20}',end='')
    else:
        print(f'R${palavra[p]:>7.2f}')