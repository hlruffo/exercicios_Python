# coding: iso-8859-1 -*-

repete = 'sim'
while repete == 'sim':
    frase = str(input('Digite uma frase para saber se é palindroma: ')).upper().strip()
    separa = frase.split()
    junto= ''.join(separa)
    reverso =''
    for letra in range(len(junto)-1,-1,-1):
        reverso += junto[letra]
    if reverso == junto:
        print(f'A frase {frase} é palindroma pois sem os espaços fica: {junto} sendo igual ao ler de trás pra frente: {reverso}')
    else:
        print(f'A frase {frase} não é palindroma pois sem os espaços fica: {junto} sendo diferente de ao ler de trás pra frente: {reverso}')

    repete = input ('Avaliar outra frase? Digite sim ou não: \n').lower ( )
    while repete != 'sim' and repete != 'não':
            repete = input('Opção inválida ? Digite sim ou não: \n').lower()
print('Até a próxima!')
