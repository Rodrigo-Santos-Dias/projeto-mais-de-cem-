notas50 = notas20 = notas10 = notas5 =notas2 = notas1 = 0
from time import sleep
print('='*20)
print('BANCO DO...')
sleep(2)
print('SEU PAI!!!!')
print('='*20)
saquerestante = int(input('Qual sera o valor a ser sacado? '))
saque=saquerestante
if saquerestante >= 50:
    while saquerestante >=50:
        saquerestante-=50
        notas50+=1
if notas50 > 0:
    print(f'Total de {notas50} notas de R$50')
if saquerestante<=49:
    while saquerestante>=20:
        saquerestante-=20
        notas20+=1
if notas20 > 0:
    print(f'Total de {notas20} notas de R$20')
if saquerestante <=19:
    while saquerestante>=10:
        saquerestante-=10
        notas10+=1
if notas10 > 0:
    print(f'Total de {notas10} notas de R$10')
if saquerestante <=9:
    while saquerestante>=5:
        saquerestante-=5
        notas5+=1
if notas5 > 0:
    print(f'Total de {notas5} notas de R$5')
if saquerestante<=4:
    while saquerestante>=2:
        saquerestante-=2
        notas2+=1
if notas2 > 0:
    print(f'Total de {notas2} notas de R$2' )
if saquerestante<=3:
    while saquerestante>=1:
        saquerestante-=1
        notas1+=1
if notas1>0:
    print(f'Total de {notas1} notas de R$1')
print('='*20)
print('Volte sempre ao Banco do seu pai!!!')



