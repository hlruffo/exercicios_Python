from Models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3, 4]: '))
    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado da seguinte conta: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} pontos')

    continuar: int = int(input('Deseja continuar? [1- sim 0- não ]'))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} pontos. Até a proxima!')


if __name__ == '__main__':
    main()