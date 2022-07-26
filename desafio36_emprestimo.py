nome_do_cliente = str(input('Qual seu nome?')).title().strip()
print(f'Olá {nome_do_cliente} Vamos descobrir se será possìvel realizar seu emprèstimo ')
valor_da_casa = float(input('Qual o valor da casa?'))

salario = float(input('Qual o salário?'))
anos = int(input('Em quantos anos  pretende concluir o pagamento?'))
parcela = anos*12
prestacao = valor_da_casa/parcela
if prestacao > 30*salario/100:
    print(f'Infelizmente não será possível disponibilizar o emprestimo pois o valor da prestação será de R${prestacao:.2f} e esse valor excede 30% do seu salário ')
else:
    print(f'{nome_do_cliente} seu empréstimo foi aprovado!\nA prestação será de {prestacao:.2f}')
