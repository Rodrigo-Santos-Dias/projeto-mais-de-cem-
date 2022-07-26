def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        print(f'Com {idade} anos o voto é:NEGADO')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos o voto é:OPCIONAL')
    else:
        print(f'Com {idade} anos o voto é:OBRIGATORIO')



nascimento = int(input('Data de nascimento: '))
voto(nascimento)
