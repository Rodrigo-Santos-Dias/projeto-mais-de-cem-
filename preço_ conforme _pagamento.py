print('Vamos calcular o valor do produto com base na forma de pagamento')
preço_do_produto = float(input((f'Digite o preço do produto')))
forma_de_pagamento = int(input(f'''Escolha a forma de pagamento:
[1] Á vista no dinheiro.
[2] Á vista no cartão.
[3] 2 vezes  no cartão.
[4] 3 vezes ou mais no cartão.
'''))
if forma_de_pagamento == 1:
    print(f'Á vista no dinheiro o produto tem um desconto de 10%, o total á ser pago é R${preço_do_produto-(10*preço_do_produto/100):.2f}')
elif forma_de_pagamento == 2:
    print(f'A vista no cartão o produto tem um desconto de 5%, o total á ser pago é R${preço_do_produto-(5*preço_do_produto/100):.2f}')
elif forma_de_pagamento == 3:
    print(f'Em duas vezees no cartão o produto não tem desconto. o total a ser pago é de {preço_do_produto:.2f}')
elif forma_de_pagamento == 4:
    parcela = int(input(f'Em quantas vezes ?'))
    print(f'Em {parcela} vezes no cartão terá um acréscimo de 20%. O total á ser pago é de {preço_do_produto+(20*preço_do_produto/100)} com parcelas de {(preço_do_produto+(20*preço_do_produto/100))/parcela:.2f}')
else:
    print(f'Opção inválida o preço á ser pago é de R${preço_do_produto}')