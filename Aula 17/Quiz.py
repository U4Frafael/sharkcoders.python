from random import randint
while True:
    pergunta = randint(0, 3)

    match pergunta:
        case 1:
            print(' Qual foi o primeiro país a começar as Grandes Navegações do século 15?: \n', "a) Portugal\n", "b) Espanha\n", "c) Inglaterra")
            resposta1 = (input("Escolha entre as opções: "))
            if resposta1 == "a":
                print("Acertou, parabéns.")
                break
            else:
                print("Tente novamente.")
        case 2:
            print('Qual o nome do instrumento muito utilizado no gênero Reggae, que lembra um violão pequeno?: \n', "a) Banjo\n", "b) Violino\n", "c) Ukelele")
            resposta2 = (input("Escolha entre as opções: "))
            if resposta2 == "c":
                print("Acertou, parabéns.")
                break
            else:
                print("Tente novamente.")
        case 3:
            print('Qual é o nome dado ao processo de mudança da água do estado gasoso para o líquido? : \n', "a) Condensação\n", "b) Fusão\n", "c) Solidificação")
            resposta3 = (input("Escolha entre as opções: "))
            if resposta3 == "a":
                print("Acertou, parabéns.")
                break
            else:
                print("Tente novamente.")