# a sequência de fibo tem inìcio no numero um(1) e sua sequência ou seu prroximo conciste na so soma no numero da sequencia
#com seu anterior exemplo o primeiro numero é (1) e o seu sequente é a soma deste (1) com seu aneterior que é zero(0)então o segundo na sequencia é
#1+0 que é igual a (1) e o terceiro é o resultado desta soma mais o seu antecessor ou seja 1+1=2 e o terceir é a soma deste resultado mais o seu anterior
# ou sesja 2 +1=3
primeiro = 0
anterior = 1
cont = 2
sucessor = primeiro+anterior

termo = int(input('Quantos termos deseja ver? '))
print('0,1',end='')
while cont <termo:
    cont+=1
    anterior = primeiro
    primeiro =  sucessor
    sucessor = primeiro + anterior
    #print(f'{sequencia}')
    print(f',{sucessor}',end='')
print('->fim')





