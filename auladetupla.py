#tuplas sâo imutaveis
lanche = ('hamburguer','suco','pizza','pudim')
#fatiamento
print(lanche[1])#tamanho da tupla
#organizado em ordem alfabetica
print(sorted(lanche))
#laço
for comida in lanche:
    print(f'eu vou comer{comida}')
#laços eposiçoes
#acesso a elementos da tupla
for cont in range(0,len(lanche)):
    print(f' eu vou comer{lanche[cont]} na posiçac  {cont}')
#acesso a elementos da tupla
for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posiçâo {pos}')
a = (2,5,4)
b = (5, 8, 1,2)
d = a+b
print(d)
print(len(d))
print(d.count(9))
#em que posiÇão
print(d.index(8))
pessoa = ('Gustavo',39, 'M',99.88)
print(pessoa)
#apagar tupla
del (pessoa)