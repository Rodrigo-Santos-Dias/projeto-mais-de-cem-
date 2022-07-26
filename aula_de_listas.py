#comida = ['Amoeba','Sua Prima','Hamburguer','suco','Seu pai']
#print(comida[2])
#valores = list(range(4,11))
#print(valores)
valores = list()
continuar= ''
while True:
    valores.append(int(input('Valores: ')))
    continuar = str(input('Continuar? ')).upper()
    while continuar not in 'Ss''Nn':
        continuar =str(input('Continuar? ')).upper()
    if continuar =='N'or continuar == 'n':
        break
#porcoes= list()
#porcoes.append(5)
#porcoes.append(3)
#porcoes.append(6)
porcoes =list()
for i in range(1,6):
    porcoes.append(int(input('Valor: ')))
for c , p in enumerate(porcoes):
    print(f'Na posição {c+1} eu encontrei {p} ')