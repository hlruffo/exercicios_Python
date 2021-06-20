# coding: iso-8859-1 -*-
repete = 'sim'
while repete == 'sim':
    numero = int(input('Digite qual número inteiro deseja saber se é primo: '))
    cont = 0
    lista= []
    for i in range(1,numero + 1):
        calc = numero % i
        if calc == 0:
            print(f'Numero é divisível por {i}.')
            cont +=1
            lista.append(i)
    if cont == 2:
        print(f'O número {numero} pode ser dividido {cont} vezes; pelos numeros {lista}. Ele é primo.')
    else:
        print(f'O número {numero} pode ser dividido {cont} vezes; pelos números {lista}. Ele não é primo')
    repete = input('Gostaria de testar outro número? Digite sim ou não: \n').lower()

    while repete != 'sim' and repete != 'não':
            repete = input('Opção inválida ? Digite sim ou não: \n').lower()
print('Até a próxima!')

