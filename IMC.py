# coding: iso-8859-1 -*-

peso = float(input('Digite o peso em Kg:'))
altura = float(input('Digite a altura em m:'))
IMC = round(peso / (altura * altura),2)
if IMC < 18.5:
    print(f'Considerando o peso {peso} e a altura {altura} o IMC ser� {IMC}. Voc� est� abaixo do peso.')
elif IMC<25:
    print(f'Considerando o peso {peso} e a altura {altura} o IMC ser� {IMC}. Voc� est� no peso ideal.')
elif IMC < 30:
    print(f'Considerando o peso {peso} e a altura {altura} o IMC ser� {IMC}. Voc� est� com sobrepeso.')
elif IMC < 40:
    print(f'Considerando o peso {peso} e a altura {altura} o IMC ser� {IMC}. Voc� est� com obesidade.')
else:
    print(f'Considerando o peso {peso} e a altura {altura} o IMC ser� {IMC}. Voc� est� obesidade m�rbida')




