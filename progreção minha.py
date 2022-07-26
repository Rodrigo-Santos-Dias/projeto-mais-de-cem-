pt = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
quant_termo = int(input('Digite quantos termos precisa ver: '))
termos_mostrados = 1
progrecao =pt
encerrar =False
print(f'Sua progreção aritimetica com {quant_termo} com razão {ra}\n{pt}',end='')
while encerrar == False :
    mais_termos = 0
    while termos_mostrados <= quant_termo :
        termos_mostrados+=1
        progrecao += ra
        print(f'->{progrecao}',end='')
        print(end='')
    continuar = int(input('\nQanatos termos a mais quer ver? '))
    while mais_termos < continuar:
        mais_termos+=1
        progrecao+=ra
        print(f'->{progrecao}',end='')
        print(end='')
    if continuar == 0:
        encerrar=True
        continuar = False

#ver como diminuir esse  programa depois





