import colorama
from colorama import Style, Back, Fore
print(f'{Back.BLACK+Fore.BLUE+Style.BRIGHT}Dê as suas medidas para calcularmos seu índice de massa corporal')
altura = float(input(f'Dê a sua altura em metros:'))
peso = float(input(f'Dê o seu peso:'))
imc = peso/(altura*altura)
if imc < 18.5:
    print(f'O seu IMC è de {imc:.2f} você está abaixo do peso:')
elif imc >18.5 and imc < 26:
    print(f'O seu IMC é de {imc:.2f} você está com o peso ideal')
elif imc > 25 and imc < 30:
    print(f'O seu IMC ´de {imc:.2f} você está com sobrepeso')
elif imc >31 and imc < 40:
    print(f'O seu IMC é de {imc:.2f} você está na faixa consederada com obesidade')
else:
    print(f'O seu IMC é de {imc:.2f} já atingiu a faixa de obesidade mórbida')
