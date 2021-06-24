repete = 'sim'
# REPETIR TODO PROGRAMA
while repete == 'sim':
    inicio = int(input('Informe o primeiro termo da sua PA: '))
    razao = int(input(('Informe a razão da PA: ')))
    cont = 0
    mais = 10
    total = 0
    print(f'Os termos da PA com início em {inicio}  e razão {razao} são:')
    #RODAR A PA ATÉ ZERO SER DIGITADO
    while mais != 0:
        total = total + mais
        #MONTAR A PA
        while cont < total:
            print(f'{inicio}', end=' -> ')
            inicio = inicio + razao
            cont += 1
        print('Feito.')  # FIM DO 3 WHILE
        #PARAMETRO PARA SAIR DO 2 WHILE; SE DIFERENTE DE 0 ENTRA NO 3 WHILE, SE NÃO SAI DO 2 WHILE E ENCERRA
        mais = int(input('Gostaria de adiciona mais termos? Digite quantos termos ou 0 para encerrar: '))

    # AO SAIR DO SEGUNDO WHILE
    print (f'\nPrograma encerrado com {total} números impressos.\n')


    # REPETIR TODO PROGRAMA -> PARAMETRO DE SAIDA DO 1 WHILE; SE FOR SIM, REPETE TUDO; SE NÃO ENCERRA O PROGRAMA
    repete = input('Gostaria de avaliar outra PA? Digite sim ou não: ').lower()
    while repete != 'sim' and repete != 'não':
        repete = input('Comando inválido. Digite sim ou não: ').lower()
#AO SAIR DO 1 WHILE ( QUANDO REPETE RECEBE NÃO )
print('Até a próxima.')
