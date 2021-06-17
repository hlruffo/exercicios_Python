from random import randint
print("Digite 'S' para lançar o dado ou 'N' para sair: ")
ordem = input()
while(ordem != 'N'):
    if ordem == 'S':
        print(randint(1, 6))
    else:
        print('Comando inválido')
    print ("Digite 'S' para lançar o dado ou 'N' para sair: ")
    ordem = input()
print("Fim")