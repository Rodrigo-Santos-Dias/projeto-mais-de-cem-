def ficha(a='<<desconhecido>>', b=0):
    print(f'O jogador {a} fez {b} gol(s) no campeonato')


nome_do_jogador = str(input('Nome do jogador: '))
gols = str(input(f'Quantos gols fez? '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome_do_jogador.strip() =='':
    ficha(b=gols)
else:
    ficha(nome_do_jogador,gols)

