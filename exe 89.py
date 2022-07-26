dados = []
lista = list()
while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 =float(input('Primeira nota: '))
    nota2 =float(input('Segunda  nota: '))
    media = (nota1+nota2)/2
    continuar = str(input('DEseja continuar? [S/N]')).strip().upper()
    if continuar not in 'Ss''Nn':
        while continuar not in 'Ss''Nn':
            continuar = str(input('DEseja continuar? [S/N]')).strip().upper()
    dados.append(nome)
    dados.append(nota1)
    dados.append(nota2)
    dados.append(media)
    lista.append(dados[:])
    dados.clear()
    if continuar in 'Nn':
        break
print('=-'*30)
print(f'{"Id":<4}{"Nome":<10}{"Media":>8}')
for pos, i in enumerate(lista) :
    print(f'{pos:<4} {i[0]:<10} {i[3]:>8}')
while True:
    notas = int(input('mostrar as notas de qual alunno? (999 interrompe): '))
    parar = notas
    if parar == 999:
        break
    if notas > len(lista)+1 :
        while notas > len(lista)+1:
            print('Dado não encontrado tente novamente.')
            notas = int(input('mostrar as notas de qual alunno? (999 interrompe): '))
    print(f'Notas de {lista[notas][0]} sâo {lista[notas][1:3]}')
print('=-'*30)


