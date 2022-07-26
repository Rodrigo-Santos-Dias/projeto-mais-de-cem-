encerrar = False
num = 0
while encerrar== False:
    cont=0
    num = int(input('Quer ver qua tabuada? '))
    print(f'Tabuada do {num}')
    if num < 0:
        encerrar = True
        break
    while cont<10:
        cont+=1
        print(f'{num} X {cont} = {num * cont}')





