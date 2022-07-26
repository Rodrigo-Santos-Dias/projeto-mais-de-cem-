def leiaint(mensg):
    ok = False
    valor = 0
    while True:
        n = str(input(mensg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro valor invalido.\033[m')
        if ok:
            break
    return valor





n = leiaint('Digite um número')
print(f'Voce digitou o número {n}')