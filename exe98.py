from time import sleep


def contador(i, f, p):
    print(f'contagem de{i} até {f} de {p} em {p}')
    if f > i:
        cont = i
        while cont <= f:
            print(f'{cont}',end=' ')
            sleep(0.5)
            if p < 0:
                p = p*-1
            if p == 0:
                p = 1
            cont+=p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            if p < 0:
                p = p*-1
            if p == 0:
                p = 1
            cont-=p
        print('FIM!')



contador(1,10,1)
contador(10,0,2)
contador(8,100,-2)
print('Agora é a sua vez de personalizar a contagem')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo:' ))
contador(i,f,p)