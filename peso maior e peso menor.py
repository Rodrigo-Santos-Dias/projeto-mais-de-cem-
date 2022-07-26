me = 0
ma = 0
pi = 0
pm = 0
for n in range(1,6):
    peso = float(input(f'{n} Pessoa digite seu peso: '))
    if peso > ma:
        ma = peso
        me = peso
    if peso == ma:
            pi +=1
    if peso < me:
        me = peso
        if peso == me:
            pm += 1
print(f'Temos o total de {pi} maiores')
print(f'Temos o total de {pi} pesos menores')
print(f'O maior peso peso é Kg{ma}\nO menor peso é Kg{me} ')
