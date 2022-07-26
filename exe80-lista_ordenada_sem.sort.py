#ler s numeros e cadastra_lo na lista ja na posição correta sem o sort
#1-> ler 5 numeros
lista = list()
for n in range(1, 6):
    numero = int(input(f'Digite um valor: '))
    if n == 1 or numero > lista[-1]:
        lista.append(numero)
    else:
        pos =0
        while pos< len(lista):
            if numero <= lista[pos]:
                lista.insert(pos,numero)
            pos += 1
            break



print(lista)


