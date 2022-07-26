#nâo terminado
num = list()
posmai =list()
posmen = list()
maior = menor = ''
for i,pos in enumerate(range(0,5)):
    num.append(int(input(f'Digite um nùmero na posição {i}: ')))
    posmen.append(pos)
    posmai.append(pos)
    if len(num) == 1:
        maior = menor = num[0]
    else:
        if num[i] > maior:
            maior = num[i]
        if num[i] < menor:
            menor = num[i]
    if menor in num:
        posmen.append(pos[menor])
    else:
        print()
 #   if maior in num:

print(f'Você digitou os valores{num}')
print(f'O maior número digitado foi {maior} nas posições{posmai}')
print(f'O menor número digitado foi {menor} nas posições {posmen}')

# print(f'Você digitou os valores{num} .{maior} x {menor}')

# for pos,c in enumerate(num):
#  if pos+1 ==1:
#     maior= menor= c
#    if c >maior:
#       maior =c
#  if c < menor:
#     menor =c
# print(f'num {maior} e{menor} ')
# print(max(num))
# for c,pos in enumerate(num):
#   print(f' o que é isso {c} e isso{pos}?')
