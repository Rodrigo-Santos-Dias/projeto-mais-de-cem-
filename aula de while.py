r = 'S'
while r =='S':
    num = int(input('numero: '))
    r = str(input('quer continuar[S/N]?')).upper()
print('Osvaldo')
# acima flag
n1= 1
while n1 != 0:
    n1 = int(input('digite um número: '))
print('Meu pai')
n2 = 1
par = impar = 0
while n2 != 0:
    n2 = int(input('valor: '))
    if n2 !=0:
        if n2 % 2==0:
            par+=1
        else:
            impar+=1
print(f'você digitou {par} numeros pares e {impar} numeros impares')
#nessa forma eu uso uma condicinal para o progrma desconsiderar o flag