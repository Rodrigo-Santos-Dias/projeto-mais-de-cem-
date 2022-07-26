from time import sleep
c = ('\033[m', #0->sem cor
        '\033[0;30;41m',#1 - >vermelho
        '\033[0;30;42m',#2 - >verde
        '\033[0;30;43m',#3 - >amarelo
        '\033[0;30;44m',#4 - >azul
        '\033[0;30;45m',#5 - >roxo
        '\033[7;;30m'   #6 - > barnco
        )

def titulo(msg,cor =0):
    tam  = len(msg)+4
    print(c[cor],end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0],end='')


def ajuda():
     while True:
        f = str(input('Qual função deseja saber? ')).strip().lower()
        if f == "fim":
            print('Fim do programa')
            break
        print(f'Acessando manual do comando "{f}" ')
        sleep(1)
        print(help(f))

   # sleep(1)


ajuda()


def outrajuda(com):
    titulo(f'Acessando manual do comando\'{com}\'',5)
    help(com)


comando = ''
while True:
    comando = str(input('Função Biblioteca >')).strip().lower()
    if comando == 'fim':
        print('Fim do programa...')
        break
    else:
        outrajuda(comando)

