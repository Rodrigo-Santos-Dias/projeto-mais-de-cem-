f = str(input(f'Digite uma frase')).strip().upper()
p = (''.join(reversed(f))).strip().upper()
if ''.join(reversed(f)) == p:
        print(f'{f} é um palindromo')
else:
    print(f'{f} não é um palindromo')