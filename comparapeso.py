# coding: UTF-8 -*-
maior = 0
menor = 0
repete = 'sim'
while repete == 'sim':
    for p in range(1,6):
        peso = float(input(f'Insira o peso da {p}ª pessoa: '))
        if p == 1:
            maior = peso
            menor = peso
        else:
            if peso > maior:
                maior = peso
            if peso < menor:
                menor = peso

    print(f'Dentre os pesos informados o maior foi {maior} kg e o menor {menor} kg.')
    repete = input('Gostaria de avaliar outra lista? Digite sim ou não: ')
    while repete != 'sim' and repete != 'não':
        repete = input('Comando inválido. Digite sim ou não: ')
print('Programa encerrado. Até a próxima.')
