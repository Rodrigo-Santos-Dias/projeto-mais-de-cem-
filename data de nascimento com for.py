from datetime import date
hoje  = date.today().year
c = 0
idade = 0
m =0
for n in range(1,8):
    nasc = int(input(f'número {n} Digite seu ano de nascimento: '))
    idade = hoje - nasc
    if idade>18:
        c+=1
        n = c
    elif idade <18:
        m +=1
        n = n
print(f'São {c} maiores de idade e {m} menores de idade')

# colocar depois quais são as menores de idade


