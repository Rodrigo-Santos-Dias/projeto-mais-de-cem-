#dessa forma usamos o (for)
f = str(input(f'Digite um número: ')).strip().upper()
p = f.split()
jun = ''.join(p)
inv = ''
for letra in range (len(jun) -1, -1, -1):
    inv += jun[letra]
if inv == jun:
    print(f'palindromo')
else:
    print(f'não palindromo')
#dessa forma usamos o fatiamnto da string
f = str(input(f'Digite um número: ')).strip().upper()
p = f.split()
jun = ''.join(p)
inv = jun[::-1]
if inv == jun:
    print(f'palindromo')
else:
    print(f'não palindromo')
