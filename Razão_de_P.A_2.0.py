pt = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
qant_termo = 1
pa = pt
encerrar = False
print(pt, end='')
while qant_termo < 10:
    pa += ra
    qant_termo += 1
    print(f'->{pa}', end='')
    mais_termos = 0
while encerrar == False:
    mais_termos = int(input('\nQantos termos a mais quer ver? '))
    mais_termos += 1
    pa+=ra
    if mais_termos == 0:
        encerrar=True



