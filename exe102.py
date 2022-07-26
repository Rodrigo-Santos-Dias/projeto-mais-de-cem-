def fatorial(num=1,show=False):
    '''

    -->calcular fatorial de um número
    :param num: valor a ser calculado
    :param show: Por padrão (show = False) parametro opcional para mostrar (show=True) ou não mostrar(show=False)
    :return: retorna o fatorial f
    '''
    f = 1
    for c in range(num,0,-1):
        f*=c
        if show :
            print(f'{c} X' if c >1 else f'{c} =', end=' ' )
    return f
    # print('=')
    #print(f'{f}')



n = int(input('Digite um numero: '))
print(fatorial(n,show=True))
help(fatorial)