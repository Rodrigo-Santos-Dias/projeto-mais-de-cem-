dados = list()
jogador = dict()
id = 0
while True:
    jogador["id"]= id
    jogador["nome"]= str(input('Nome do jogador' )).strip().title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador["gols"]=list()
    for c in range(1, partidas+1):
        jogador["gols"].append(int(input(f'    Quantos gols na  partida {c} ?')))
    jogador["total"] = sum(jogador["gols"])
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    id +=1
    while continuar not in 'Ss''NN':
        print('Tente novamente:')
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    dados.append(jogador.copy())
    if continuar in 'Nn':
        break
print('-=' * 30)
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-' * 30)
for k ,v in enumerate(dados):
    for d in v.values():
        print(f'{str(d):<12}',end=' ')
    print()
print('-' * 30)
while True:
    mostrar_dados = int(input('Dseja mostra os dados de qual jogador? (999 para parar) '))
    if mostrar_dados == 999:
        print('Fim do programa')
        break
    if mostrar_dados >= len(dados):
        if mostrar_dados> len(dados):
            print("jogador não encontrado")
    else:
        print(f'Levantamento do jogador {dados[mostrar_dados]["nome"]} ')
        if mostrar_dados <= len(dados):
            for pos, i in enumerate(dados[mostrar_dados]["gols"]):
                print(f'Na partida {pos + 1} fez {i} gols')
            print('-'*30)
print('<< Volter sempre>>')




