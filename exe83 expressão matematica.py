invalida = 0
lista=list((str(input('Digite aqui sua expressão matematica: '))))
if lista[0] == ')' or lista.count('(') != lista.count(')'):
    invalida +=1
for i in range(0,len(lista)):
    if lista[i]== ')' and lista[i-1] == '*-+=':
        invalida += 1
if invalida == 0:
    print('Sua expressão é valida!!!')

else:
    print('Sua expressão é invalida!!!')