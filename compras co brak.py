produto_maisbarato = ''
produto_mais_de_mil = cont= total = menorpreco = 0
continuar = ''
from time import sleep
print('{:-^40}'.format('LOja do...'))
sleep(2)
print('{:-^40}'.format('SEU PAI!!!'))
while True:
    produto = str(input('produto: '))
    preco = float(input('preço: R$'))
    cont+=1
    total+=preco
    continuar = str(input('desja continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'S''N':
        continuar = str(input('desja continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
    if preco>1000:
        produto_mais_de_mil+=1
    if cont == 1 or preco<menorpreco:
        menorpreco= preco
        produto_maisbarato= produto
print(f'O valor total da compra foi de R${total:.2f}\n{produto_mais_de_mil} é a quantidade de produtos custando mais de R$ 1000.00')
print(f'{produto_maisbarato} Foi o produto mais barato custando R${menorpreco:.2f}')
print('{:-^40}'.format('Fim do prgrama'))