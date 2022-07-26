numero = int(input('Digite um número para descobrir seu fatorial: '))
bob = 1
for c in range (numero,0,-1):
    bob *= c
    print(f'{c}x' if c > 1 else f'{c}=',end='')
print(bob)
#bob é  nome aleatório da variavel para receber a multiplicação
#primeiro a  variavel (bob, no cso) vai receber 1 que ´eo numero neutr da multiplicação
# toda vez que o range de  numero até 1 acontecer  a variavél  (bob) vai receber (bob X bob X o numero -1)