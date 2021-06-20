# coding: iso-8859-1 -*-
from datetime import date

repete = 'sim'
while repete == 'sim':
    maior = []
    menor =[]
    atual = date.today().year
    for numero in range(1,8):
        nascimento = int(input(f'Digite o ano de nascimento da pessoa {numero} com 4 dígitos:'))
        idade = atual - nascimento
        if idade >= 18:
            maior.append(numero)
        else:
            menor.append(numero)
    maior_str = str(maior)[1:-1]
    menor_str = str(menor)[1:-1]
    print(f'Na lista há {len(maior)} pessoas maiores de idade, sendo elas {maior_str}')
    print(f'Na lista há {len(menor)} pessoas menores de idade, sendo elas {menor_str}')

    repete = input('Avaliar outro grupo? Digite sim ou não: \n').lower()
    while repete != 'sim' and repete != 'não':
            repete = input('Opção inválida ? Digite sim ou não: \n').lower()
print('Até a próxima!')
