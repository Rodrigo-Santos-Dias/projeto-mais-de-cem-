from time import sleep
def maior(* num):
    print('=-'*25)
    print('Analisando os numeros...')
    maior_num = 0
    quantermos = 0
    for pos, item in enumerate(num):
        print(item ,end= ' ')
        quantermos+=1
        sleep(1)
        if num[pos]> maior_num:
            maior_num = num[pos]
    print(f'foram pasados {quantermos} números\nO maior numero é {maior_num} ')


maior(9,3,7,4,2)
maior(3,7,0,4)
maior(2,1,3)
maior()