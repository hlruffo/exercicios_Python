from random import randint
repete = 'sim'
while repete == 'sim':
    numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
    print('Os números sorteados foram:')
    for n in numeros:
        print(f'{n}', end=' ')
    print(f'. O maior valor é {max(numeros)} e o menor {min(numeros)}')

    repete = input('Gostaria de sortear de novo? Digite sim ou não: ').lower()
    while repete != 'sim' and repete != 'não':
        repete = input('Comando inválido. Digite sim ou não: ')

print('Programa encerrado. Até a próxima.')

