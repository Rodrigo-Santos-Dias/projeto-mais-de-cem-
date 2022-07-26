valores = (int(input('Digite um nùmero: ')),int(input('Digite mais um nùmero: ')),int(input('Digite outro nùmero: ')),int(input('Digite o ultimo nùmero: ')))
print(f'Você digitou os valores {valores}')
if valores.count(9)==0:
    print(f'O valor 9 não foi digitado')
elif valores.count(9)==1:
    print(f'O valor 9 foi digitado apenas 1 vez')
else:
     print(f'O valor 9 foi digitado o total de {valores.count(9)} vezes')
# solução prof
#if 3 in valores:
#    print (o valor apareceu na primeira vez em {valores.index(3)+1})
#else:
#print ('o valor 3 não apareceu')
if valores[0:].count(3) == 0 :
    print(f'O valor 3 não apareceu em nenhuma posição')
else:
    print(f'O valor 3 apareceu pela primeira vez na posição {valores.index(3)+1}')
print('Os numeros pares são ', end= '')
for v in valores:
    if v%2==0:
        print(v,end=' ')





