# coding: iso-8859-1 -*-
import random
from time import sleep

jogar ='sim'
print("_________________________")
print("!!Bem-vindo ao Jokenpo!!")
print("_________________________")
resultado = ['Vit�ria do CPU!', 'Houve um empate!', 'O usu�rio venceu!']
jogadas = ['pedra', 'papel', 'tesoura']
pontos_user = 0
pontos_cpu = 0

while jogar == 'sim':

    user = input(f'Escolha uma jogada entre {jogadas}:  ').lower()
    if user not in jogadas:
        user = input (f'As jogadas v�lidas s�o {jogadas}. Escolha uma entre elas: ').lower()

    print('Pronto?')
    cpu = random.choice(jogadas)
    sleep(3)
    print('Processando jogadas!')
    sleep(2)
    #               0        1         2
    #jogadas = ['pedra', 'papel', 'tesoura']
    #resultado = ['Vit�ria do CPU!', 'Houve um empate!', 'O usu�rio venceu!']
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

    print(f'Usu�rio escolheu {user} e CPU {cpu}.{caso} Placar: Usu�rio {pontos_user} x CPU {pontos_cpu}.')
    jogar = input('Gostaria de jogar novamente? Digite sim ou n�o:').lower()
    if jogar != "sim" and jogar != "n�o":
        jogar = input('Op��o inv�lida! Gostaria de jogar novamente? Digite sim ou n�o: \n').lower()

if pontos_cpu > pontos_user:
    print(f'Placar final: Usu�rio {pontos_user}x CPU {pontos_cpu}. Vit�ria do CPU. Melhor sorte na pr�xima vez!')
elif pontos_user > pontos_cpu:
    print(f'Placar final: Usu�rio {pontos_user}x CPU {pontos_cpu}. Parab�ns!!!! Voc� venceu!! At� a pr�xima')
else:
    print(f'Placar final: Usu�rio {pontos_user}x CPU {pontos_cpu}. Desta vez empatamos! At� a pr�xima!')


