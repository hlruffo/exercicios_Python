# coding: iso-8859-1 -*-
from datetime import date

repete = 'sim'
while repete == 'sim':
    maior = []
    menor =[]
    atual = date.today().year
    for numero in range(1,8):
        nascimento = int(input(f'Digite o ano de nascimento da pessoa {numero} com 4 d�gitos:'))
        idade = atual - nascimento
        if idade >= 18:
            maior.append(numero)
        else:
            menor.append(numero)
    maior_str = str(maior)[1:-1]
    menor_str = str(menor)[1:-1]
    print(f'Na lista h� {len(maior)} pessoas maiores de idade, sendo elas {maior_str}')
    print(f'Na lista h� {len(menor)} pessoas menores de idade, sendo elas {menor_str}')

    repete = input('Avaliar outro grupo? Digite sim ou n�o: \n').lower()
    if repete != 'sim' and repete != 'n�o':
            repete = input('Op��o inv�lida ? Digite sim ou n�o: \n').lower()
print('At� a pr�xima!')
