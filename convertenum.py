# coding: iso-8859-1 -*-

#programa para converter numero inteiro em binario, octal ou hexadecimal

again = 'sim'
while again == 'sim':
    conv = ['binário','binario', 'octal', 'hexadecimal']
    num = (input('Insira o número que deseja converter:'))
    while not num.isdigit():
        num = (input('Você precisa inserir um número! Digite um número para conversão: '))

    formato = input('Insira formato de saida entre binário, octal ou hexadecimal: ').lower()
    while formato not in conv:
        formato = input(f'Este não é um formato aceito. É possível converter para os seguintes formatos:{conv}. Escolha um formato: \n').lower()

    num = int(num)
    if formato in conv[0] or formato in conv[1]:
        num_convertido = bin(num)
    elif formato in conv[2]:
        num_convertido = oct(num)
    else:
        num_convertido = hex(num)
    num_convertido = str(num_convertido)
    print(f'O número inserido convertido para {formato} é {num_convertido[2:]} \n') #[2:] retira os dois primeiros digitos impressos referente ao tipo 

    again = input("Gostaria de converter outro número? Digite sim ou não: \n").lower()

print("Obrigado por usar o nosso app!")