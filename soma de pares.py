#laço de input
c = 0
s = 0
for i in range(1,7):
    n = int(input(f'Digite o {i} valor:'))
    if n % 2 == 0:
        s += n
        c += 1
print(s)

#programa deve ler seis numeros inteiros e mostrar na tela apenas a soma dos numeros pares
# se os valor for digitado impar desconsidera
#explicação: para que o programa leia 6 numeros inteiros eu preciso de um laço em uma variavel de 1 ate 6 +1 (por que ele vai contar de 1 que é o começo
#até o fim do 5 e para no 6 sem cont lo então adiciona  mais um)
# que terá uuma viravel (n) de input  de números inteiros (int)
# para somar os apenas os pares ignorando os impares eu preciso de uma condiocional (if) para os pares serem somamdos(s) e para contar a quatidade de pares dentro da estrtura if uso um contador(c)
