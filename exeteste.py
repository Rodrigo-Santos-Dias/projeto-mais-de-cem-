def leiafloat(mensagem):
    valor = 0
    while True:
        try:
            n = str(input(mensagem)).replace(',', '.')
            n = float(n)
        except ValueError :
            print(f'Dado inválido')
            continue
        except KeyboardInterrupt:
            print('O usuario decidiu não informao um valor')
            return valor
        else:
            valor = float(n)
            return valor





num = leiafloat('digite um número:')
print(f'o valor digitado foi {num}')