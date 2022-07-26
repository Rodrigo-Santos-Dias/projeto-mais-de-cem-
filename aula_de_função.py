#como crir docstring
def somar(a=0, b=0, c=0):
    """
    ->Faz uma soma de três valores mostra o resultado na tela
    :param a: Primeiro valor informado
    :param b: segundo  valor informado
    :param c: Terceiro valor informado
    :return: o valor da soma
    :resultado s : Soma dos três valores
    """
    s = a+b+c
    return s



#r1 = somar(3,8,0)
#r2 = somar(8,7)
#r3 = somar(2)
#print(f'Os resultados foram {r1}, {r2} e {r3}')

#help(somar)
# escopo de varaiveis


def teste(b):
    b+=4
    #c+=2
    x = 8
    print(f'Na função teste o n vale {n}')
    print(f'Na função teste o x vale {x}')
    print(f'Na função teste o b vale {b}')


# programa pricipal
#j = 6
#n= 2
#print(f'No programa principal o n vale{n}')
#teste(j)
#print(f'No programa principal o x vale{x}')
# o valor  de x neste caso nao pode ser printado pelo programa principal porque x esta em um escopo local dentro da funçaão teste


def fatorial(num=1):
    f = 1
    for c in range(num,0,-1):
        f*=c
    return f

#n = int(input('Digite um numero para saber o fatorial:'))
#print(f"O fatorial de {n} é igual a {fatorial(n)}")
def par (n=0):
    if n % 2 ==0:
        return True
    else:
        return False


num = int(input('Digite um mumero:'))
if par(num):
    print(f'O numero {num} é par')
else:
    print(f'O numero {num} não é par')
    