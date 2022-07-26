total = 0
produto_mais_de_cem= 0
continuar = ''
produto_mais_barato =''
menor_preco = cont =  0
while True:
    produto = str(input('Nome do produto: ')).strip().title()
    try:
        preco = float(input('Preço: '))
        total+=preco
        cont+=1
        if preco > 100:
            produto_mais_de_cem += 1
        if cont == 1:
            menor_preco = preco
            produto_mais_barato = produto
        else:
            if preco <= menor_preco:
                menor_preco = preco
                produto_mais_barato = produto
    except ValueError:
        print('Dado invalido.')
        preco = float(input('Preço: '))
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while continuar not in 'S''N':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print(f'O total da compra foi de R${total}\n{produto_mais_de_cem} é o total de produtos custando mais de cem reais\n{produto_mais_barato} foi o produto mais barato da lista custando {menor_preco}')
print('Fim do prgrama')
