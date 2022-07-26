lista  =['Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','oito','nove','Dez','Onze','Doze','Treze','Quatoze','Quinze','Dezeseis','Dezesete','Dezoito','Dezenove','Vinte']
numero =int(input('Digite um numero entre Zero e Vinte: '))
while numero not in range(len(lista)):
    numero = int(input('Tente novamente. Digite um numero entre Zero e Vinte: '))
print(f'voce digitou o número {lista[numero]}')