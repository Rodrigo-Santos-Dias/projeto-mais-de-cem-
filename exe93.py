from  datetime import datetime
dado = dict()
dado["nome"] = str(input('Nome : '))
nascimento = int(input('Ano de nascimento: '))
dado["idade"] = datetime.now().year - nascimento
dado["carteira"] = int(input('Carteira de trabalho ( 0 nâo tem): '))
if dado["carteira"] == 0:
    print('=-'*30)
    for k ,v in dado.items():
        print(f'{k} tem valor {v}')
else:
    dado["contrtaÇâo"] = int(input('Ano de contrtaçâo: '))
    dado["salàrio"] = float(input('Salário R$ '))
    dado["aposentadoria"] = 35 +  (dado["contrtaÇâo"]-nascimento)
    for c, i in dado.items():
        print(f'{c} tem valor {i}')



