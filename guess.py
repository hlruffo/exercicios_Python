import random
num = random.randrange(1,10)
def validação(valor):
    try:
        int(valor)
        return True
    except:
        pass
    return False
while True:
    guess = input("Chute um número: ")
    if int(guess) == num:
        print(f'Parabéns o número era {num}')
        break
    elif int(guess) > num+3 or int(guess)< num-3:
        print("Chutou longe !")
    elif num - 3 < int(guess) < num+3:
        print("Quase!")
