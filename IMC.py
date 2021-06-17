# coding: iso-8859-1 -*-

peso = float(input('Digite o peso em Kg:'))
altura = float(input('Digite a altura em m:'))
IMC = round(peso / (altura * altura),2)
if IMC < 18.5:
    print(f'Considerando o peso {peso} e a altura {altura} o IMC será {IMC}. Você está abaixo do peso.')
elif IMC<25:
    print(f'Considerando o peso {peso} e a altura {altura} o IMC será {IMC}. Você está no peso ideal.')
elif IMC < 30:
    print(f'Considerando o peso {peso} e a altura {altura} o IMC será {IMC}. Você está com sobrepeso.')
elif IMC < 40:
    print(f'Considerando o peso {peso} e a altura {altura} o IMC será {IMC}. Você está com obesidade.')
else:
    print(f'Considerando o peso {peso} e a altura {altura} o IMC será {IMC}. Você está obesidade mórbida')




