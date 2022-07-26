aluno = dict()
aluno["nome"] = str(input('Nome do aluno:')).strip().title()
aluno["Media"]= float(input(f'Media de {aluno["nome"]}: '))
if aluno["Media"]>=7:
    aluno["situação"] = 'Aprovado'
elif 5 <= aluno["Media"]<7:
    aluno["situação"] = 'REcuperação'
else:
    aluno["situação"] ='Reprovado'
#alunos = []
#alunos.append(aluno.copy())
#for i in alunos:
for c,k in aluno.items():
    print(f'{c} é {k}')
print()
