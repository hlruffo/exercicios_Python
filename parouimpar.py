from random import randint
repete = 'sim'
print('Vamos jogar par ou impar!')
ponto_user = 0
ponto_cpu = 0
while repete == 'sim':

    user = int(input('Defina sua jogada! Escolha um número: '))
    escolha = str(input('Escolha par ou impar: ')).lower()
    cpu = randint(0, 10)
    soma = user + cpu

    resultado = soma % 2
    if resultado == 0 and escolha == 'par':
        print(f'O jogador jogou {user} e o computador {cpu}; o resultado é par. Vitória do usuário.')
        ponto_user +=1
    elif resultado == 0 and escolha == 'impar':
        print(f'O jogador jogou {user} e o compurador {cpu}; o  resultado é par. Vitória do CPU')
        ponto_cpu += 1
    elif resultado !=0 and escolha == 'impar':
        print(f'O jogador jogou {user} e o computador {cpu}; o resultado é impar. Vitória do usuário')
        ponto_user += 1
    else:
        print (f'O jogador jogou {user} e o compurador {cpu}; o  resultado é impar. Vitória do CPU')
        ponto_cpu += 1
    print(f'O placar atual é Usuario {ponto_user} x {ponto_cpu} CPU')


    repete = input('Gostaria de jogar de novo? Digite sim ou não: ').lower()
    while repete != 'sim' and repete != 'não':
        repete = input('Comando inválido. Digite sim ou não: ')

print(f'Placar final usuário {ponto_user} x CPU {ponto_cpu}', end=' ')
if ponto_user > ponto_cpu:
    print('Vitória do jogador', end='')
elif ponto_user == ponto_cpu:
    print('Houve um empate!', end=' ')
else:
    print('Vitória do CPU', end=' ')
print('Programa encerrado. Até a próxima.')
