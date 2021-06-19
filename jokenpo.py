# coding: iso-8859-1 -*-
import random
from time import sleep

jogar ='sim'
print("_________________________")
print("!!Bem-vindo ao Jokenpo!!")
print("_________________________")
resultado = ['Vitória do CPU!', 'Houve um empate!', 'O usuário venceu!']
jogadas = ['pedra', 'papel', 'tesoura']
pontos_user = 0
pontos_cpu = 0

while jogar == 'sim':

    user = input(f'Escolha uma jogada entre {jogadas}:  ').lower()
    if user not in jogadas:
        user = input (f'As jogadas válidas são {jogadas}. Escolha uma entre elas: ').lower()

    print('Pronto?')
    cpu = random.choice(jogadas)
    sleep(3)
    print('Processando jogadas!')
    sleep(2)
    #               0        1         2
    #jogadas = ['pedra', 'papel', 'tesoura']
    #resultado = ['Vitória do CPU!', 'Houve um empate!', 'O usuário venceu!']
    if user in jogadas[0] and cpu in jogadas[1] or user in jogadas[1] and cpu in jogadas[2] or user in jogadas[2] and cpu in jogadas[0]:
        result =0
    elif user == cpu:
        result = 1
    else:
        result =2
    if result == 1:
        caso= resultado[1]
    elif result == 0:
        caso= resultado[0]
        pontos_cpu +=1
    else:
        caso = resultado[2]
        pontos_user += 1

    print(f'Usuário escolheu {user} e CPU {cpu}.{caso} Placar: Usuário {pontos_user} x CPU {pontos_cpu}.')
    jogar = input('Gostaria de jogar novamente? Digite sim ou não:').lower()
    if jogar != "sim" and jogar != "não":
        jogar = input('Opção inválida! Gostaria de jogar novamente? Digite sim ou não: \n').lower()

if pontos_cpu > pontos_user:
    print(f'Placar final: Usuário {pontos_user}x CPU {pontos_cpu}. Vitória do CPU. Melhor sorte na próxima vez!')
elif pontos_user > pontos_cpu:
    print(f'Placar final: Usuário {pontos_user}x CPU {pontos_cpu}. Parabéns!!!! Você venceu!! Até a próxima')
else:
    print(f'Placar final: Usuário {pontos_user}x CPU {pontos_cpu}. Desta vez empatamos! Até a próxima!')


