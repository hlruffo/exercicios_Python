# coding: iso-8859-1 -*-

calcular = 'sim'
while calcular == 'sim':
    pagamento =['dinheiro', 'cheque', 'cart�o 1x', 'cart�o 2x', 'cart�o mais que 2x']
    forma = input('Insira sua forma de pagamento:').lower()

    while forma not in pagamento:
        print(f'Esta n�o � uma forma de pagamento aceita. S�o aceitas as seguintes formas:{pagamento} \n')
        forma = input('Insira sua forma de pagamento entre uma delas : ').lower()

    pre�o = (input('Insira o valor em Reais:'))
    while not pre�o.isdigit():
        pre�o = (input('Pre�o deve ser um n�mero. Digite o pre�o: '))

    pre�o = float(pre�o)
    pre�o = round(pre�o,2)

    if forma in pagamento[0] or forma in pagamento[1]:
        pre�o = 0.9 * pre�o
    elif forma in pagamento[2]:
        pre�o = 0.95 * pre�o
    elif forma in pagamento[3]:
        pre�o = pre�o
    else:
        pre�o = 1.2 * pre�o

    print(f'O pre�o a pagar � de {pre�o} considerando pagamento em {forma}')
    calcular = input('Gostaria de calcualar outro pre�o? sim ou n�o ').lower()

print('Obrigado por usar nosso sistema. Tenha um bom dia ')
