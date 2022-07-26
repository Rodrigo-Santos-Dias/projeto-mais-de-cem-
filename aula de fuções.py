def contador(* num):
    for valor in num:
        print(f'{valor}',end=' ')
    print()



contador(3, 1, 9)
contador(2, 8, 2)
contador(5, 3, 7)
def dobrar(list):
    pos = 0
    while pos < len(list):
        list[pos]*=2
        pos+=1


valores = [7, 5, 9, 4, 2]
dobrar(valores)
for valor in valores:
    print(valor)
