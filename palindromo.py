# coding: iso-8859-1 -*-

repete = 'sim'
while repete == 'sim':
    frase = str(input('Digite uma frase para saber se � palindroma: ')).upper().strip()
    separa = frase.split()
    junto= ''.join(separa)
    reverso =''
    for letra in range(len(junto)-1,-1,-1):
        reverso += junto[letra]
    if reverso == junto:
        print(f'A frase {frase} � palindroma pois sem os espa�os fica: {junto} sendo igual ao ler de tr�s pra frente: {reverso}')
    else:
        print(f'A frase {frase} n�o � palindroma pois sem os espa�os fica: {junto} sendo diferente de ao ler de tr�s pra frente: {reverso}')

    repete = input ('Avaliar outra frase? Digite sim ou n�o: \n').lower ( )
    if repete != 'sim' and repete != 'n�o':
            repete = input('Op��o inv�lida ? Digite sim ou n�o: \n').lower()
print('At� a pr�xima!')
