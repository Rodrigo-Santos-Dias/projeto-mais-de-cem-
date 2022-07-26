galera = list()
def leiaint(mensagem):
    valor = 0
    while True:
        try:
            n = int(input(mensagem))
        except ValueError as erro:
            print(f'Dado  inválido')
            continue
        except KeyboardInterrupt:
            print('O usuário decidiu nâo informar o valor')
            return valor
        else:
            valor = n
            return valor


def tratnome(mensagem):
    n = ''
    try:
         n = str(input(mensagem)).strip().title()
    except :
        print('Usuário Decidiu não iformar o nome')
    else:
        n =str(n)
    return n


galera.append(tratnome('Seu nome: '))
galera.append(leiaint('Sua idade:'))
print(galera)



with open('dados_pessoas.txt','w') as dados:
    for p in galera:
        dados.write(str(p))


