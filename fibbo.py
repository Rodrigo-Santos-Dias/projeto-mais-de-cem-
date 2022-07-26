num = int(input('Quantos termos quer mostrar? '))
primeiro = 0
sucessor = 1
cont =2
print('0,1,',end='')
while cont <num:
    cont+=1
    sequencia = primeiro+sucessor
    primeiro =sucessor
    sucessor = sequencia
    print(f'{sequencia},',end='')
