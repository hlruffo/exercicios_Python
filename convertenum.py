# coding: iso-8859-1 -*-

#programa para converter numero inteiro em binario, octal ou hexadecimal

again = 'sim'
while again == 'sim':
    conv = ['bin�rio','binario', 'octal', 'hexadecimal']
    num = (input('Insira o n�mero que deseja converter:'))
    while not num.isdigit():
        num = (input('Voc� precisa inserir um n�mero! Digite um n�mero para convers�o: '))

    formato = input('Insira formato de saida entre bin�rio, octal ou hexadecimal: ').lower()
    while formato not in conv:
        formato = input(f'Este n�o � um formato aceito. � poss�vel converter para os seguintes formatos:{conv}. Escolha um formato: \n').lower()

    num = int(num)
    if formato in conv[0] or formato in conv[1]:
        num_convertido = bin(num)
    elif formato in conv[2]:
        num_convertido = oct(num)
    else:
        num_convertido = hex(num)
    num_convertido = str(num_convertido)
    print(f'O n�mero inserido convertido para {formato} � {num_convertido[2:]} \n') #[2:] retira os dois primeiros digitos impressos referente ao tipo 

    again = input("Gostaria de converter outro n�mero? Digite sim ou n�o: \n").lower()

print("Obrigado por usar o nosso app!")