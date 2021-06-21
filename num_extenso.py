repete = 'sim'
while repete == 'sim':
    ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete','oito', 'nove', 'dez')
    while True:
        num = int(input('Digite um número de 0 a 10 para escrever por extenso: '))
        if 0 <= num <= 10:
            break
        print('Número inválido! Tente novamente.', end=' ')
    print(f'O número por extenso é {ext[num]}')

    repete = input('Gostaria de escrever de novo? Digite sim ou não: ').lower()
    while repete != 'sim' and repete != 'não':
        repete = input('Comando inválido. Digite sim ou não: ')

print('Programa encerrado. Até a próxima.')
