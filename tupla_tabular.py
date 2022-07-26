listagem=('Pão', 2, 'Leite',3.50, 'Lapis', 0.50, 'Sua Prima', 1.00,'Minha Prima', 50000)
print('_'*40)
print('{:^20}'.format('LISTAGEM DE PREÇOS'))
print('_'*40)
for p in range(0,len(listagem),2):
    print(f'{(listagem[p]):.<20}.......... R$ {listagem[p+1]:.2f}')
print('_'*40)


