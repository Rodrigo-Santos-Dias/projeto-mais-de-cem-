n = int(input(f'Digite o número da tabuada que quer estudar:'))
print(f'TABUADA DO {n}')
for i in range(0,11):
    print('=-=' * 5)
    print(f'{n} x {i:2} = {n*i:2}')
print('=-='*5)
#nâo precisa de contador nem acumulador: não pra tabuada pelomenos
