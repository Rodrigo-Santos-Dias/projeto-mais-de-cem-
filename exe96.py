
def mensagem(msg):
    c = 0
    for l in range(0,len(msg)+2):
        print('~',end='')
        c+=1
    print()
    print(msg)
    print('~'*c)

mensagem('Curso em video')
mensagem('CEv')
mensagem('Rodrigo')
