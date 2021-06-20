# coding: UTF-8 -*-

"""

media de idade de todos
nome do homem mais velho
qnts mulheres tem menos de 20 anos
"""


repete = 'sim'
while repete == 'sim':
    soma = 0
    nomevelho = 0
    idadevelho = 0
    media = 0
    somaidade = 0
    for p in range(1, 5):
        print(f'Insira as informações da {p}ª pessoa:')
        nome = str(input('Qual o nome? ')).strip()
        idade = int(input('Qual a idade?:'))
        sexo = str(input('Qual o sexo? F ou M: ')).strip().upper()
    #calculo da média de idade
        if p < 4:
            somaidade += idade
        else:
            media = somaidade / 4
        #nome do homem mais velho
        if sexo == 'M':
            if idadevelho < idade:
                nomevelho = nome
                idadevelho = idade
        #quantas mulheres tem menos de 20 anos
        if sexo == 'F':
            if idade < 20:
                soma += 1
    print(f'A média de idade é : {media}; o homem mais velho é {nomevelho} com {idadevelho} anos e há {soma} mulheres com menos de 20 anos.')

    repete = input('Gostaria de avaliar outra lista? Digite sim ou não: ')
    while repete != 'sim' and repete != 'não':
        repete = input('Comando inválido. Digite sim ou não: ')
print('Programa encerrado. Até a próxima.')
