# coding: UTF-8 -*-
from time import sleep
repete = 'sim'
while repete == 'sim':
    fatorial = 1
    numero = int(input('Insira um número para calcular seu fatorial: '))
    print(f'Calculando {numero}!: ')
    sleep(2)
    while numero > 0:
        fatorial = fatorial * numero
        print(f'{numero} ',end='')
        print(f' x ' if numero >1 else ' = ', end= '')
        numero -= 1
    print(f'{fatorial}')


    repete = input('Gostaria de avaliar outra lista? Digite sim ou não: ')
    while repete != 'sim' and repete != 'não':
        repete = input('Comando inválido. Digite sim ou não: ')
print('Programa encerrado. Até a próxima.')
