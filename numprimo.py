# coding: iso-8859-1 -*-
repete = 'sim'
while repete == 'sim':
    numero = int(input('Digite qual n�mero inteiro deseja saber se � primo: '))
    cont = 0
    lista= []
    for i in range(1,numero + 1):
        calc = numero % i
        if calc == 0:
            print(f'Numero � divis�vel por {i}.')
            cont +=1
            lista.append(i)
    if cont == 2:
        print(f'O n�mero {numero} pode ser dividido {cont} vezes; pelos numeros {lista}. Ele � primo.')
    else:
        print(f'O n�mero {numero} pode ser dividido {cont} vezes; pelos n�meros {lista}. Ele n�o � primo')
    repete = input('Gostaria de testar outro n�mero? Digite sim ou n�o: \n').lower()

    if repete != 'sim' and repete != 'n�o':
            repete = input('Op��o inv�lida ? Digite sim ou n�o: \n').lower()
print('At� a pr�xima!')

