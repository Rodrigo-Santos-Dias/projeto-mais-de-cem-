palavra= ('aprender','programar','linguagem','python','curso','gratis','esrtudar','praticar','trabalhar','mercado','trabalhador','futuro')
for p in palavra:
    print(f'Na palavra {p.upper()} temos' ,end=' ')
    for v in p:
        if v in 'aeiou':
            print(f'{v}',end='')
    print()
