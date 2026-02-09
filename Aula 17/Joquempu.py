from random import randint

jogador = input('pedra, papel ou tesoura?: ')
opcao = randint(0, 3)

match opcao:
    case 1:
        print('Pedra')
    case 2:
        print('Papel')
    case 3:
        print('Tesoura')


if jogador == "pedra" and opcao == 1:
    print("Impate, repita.")
elif jogador == "pedra" and opcao == 2:
    print("Perdeu, repita.")
else:
    print("Ganhou, parabéns.")
