repete = 'sim'
while repete == 'sim':
    inicio = int(input('Informe o primeiro termo da sua PA: '))
    razao = int(input(('Informe a razão da PA: ')))
    cont = 1
    print(f'Os termos da PA com início em {inicio}  e razão {razao} são:')
    while cont < 11:
        print(f'{inicio}', end=' -> ')
        inicio = inicio + razao
        cont += 1
    print ('Fim de sequência \n')
    repete = input('Gostaria de avaliar outra lista? Digite sim ou não: ')
    while repete != 'sim' and repete != 'não':
        repete = input('Comando inválido. Digite sim ou não: ')
print('Programa encerrado. Até a próxima.')
