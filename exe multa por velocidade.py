velocidade = int(input('Qual a volocidade do carro?'))
multa = (velocidade-80)*7.00
if velocidade>80:
    print('Você excedeu o limite da velocidade permitida e será multado em R${}'.format(multa))
else:
    print('Boa viajem')
    