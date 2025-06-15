#Faça um jogo do erro para calcular quantas vezes o usuário o errou para acertar o valor
import random

numero_secreto = random.randint(1, 10)
tentativas_erradas = 0
while True:
    palpite = int(input("Digite seu palpite entre 1 e 10: "))

    if palpite == numero_secreto:
        print("Parabéns! Voceẽ acertou o número ", numero_secreto )
        print("Tentativas erradas: ",tentativas_erradas)
        break

    else:
        tentativas_erradas += 1
        print("Voçẽ errou! Tente novamente")