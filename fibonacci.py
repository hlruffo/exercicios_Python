repete = 'sim'
while repete == 'sim':
    n = int(input("Quantos números da sequência você quer ver?: "))
    cont = 0
    a = 0
    b = 1
    print(f'{a} -> {b}', end=' -> ')
    while cont < n-2:
        soma = a + b
        a = b
        b = soma
        print(f' {soma}', end=" -> ")
        cont += 1
    print('FIM')
    repete = input('Gostaria de avaliar outra sequência? Digite sim ou não: ')
    while repete != 'sim' and repete != 'não':
        repete = input('Comando inválido. Digite sim ou não: ')
print('Programa encerrado. Até a próxima.')
