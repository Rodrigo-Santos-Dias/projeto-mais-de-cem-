import random
palpites = 1
computador = random.randint(0, 10)
jogador = int(input(f'Pensei em um número de 0 a 10, adivinhe qual: '))
if jogador != computador:
    print('tente novamente')
    if jogador > computador:
        print('Chutou muito alto')
    if jogador < computador:
        print('Chutou baixo demais')
while jogador != computador:
    palpites += 1
    jogador = int(input(f'Pensei em um número de 0 a 10, adivinhe qual: '))
    if jogador > computador:
        print('Chutou muito alto')
    if jogador < computador:
        print('Chutou baixo demais')
if computador == jogador:
    print(f'parabéns pensei no numero {computador} voce acertou em {palpites} tentativas')
    if palpites == 1:
        print(f'NOSSA!!! você é muito bom precisou de apenas {palpites} palpite')

