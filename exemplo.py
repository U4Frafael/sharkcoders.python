import random
import time

dinheiro = 1000

def saldo():
    global dinheiro
    print(f'Saldo Atual: {dinheiro}')
    
    valor_input = input("Valor da aposta (ou '0' para sair): ")
    if valor_input == "0":
        exit()

    valor = int(valor_input)
    if valor > dinheiro:
        print("Não tens dinheiro suficiente!\n")
        return None

    return valor
    
def slot(valor):
    global dinheiro
    opcoes = ['🍒', '💎', '7️⃣']
    
    print("A girar...", end=" ")
    for _ in range(15):
        reels_fake = [random.choice(opcoes) for _ in range(3)]
        print(f" {' | '.join(reels_fake)} ", end="\r")
        time.sleep(0.25)

    resultado = [random.choice(opcoes) for _ in range(3)]
    print(f"Resultado: {' | '.join(resultado)} \n")
 
    if resultado[0] == resultado[1] == resultado[2]:
        print("Ganhaste, parabéns!\n")
        dinheiro += valor
    else:
        print("Perdeste, tenta novamente.\n")
        dinheiro -= valor

    if dinheiro <= 0:
        print("Ficaste sem dinheiro! O jogo vai recomeçar...\n")
        dinheiro = 1000


while True:
    try:
        valor = saldo()

        if valor is None:
            continue

        slot(valor)

    except ValueError:
        print("Por favor, insira um número válido.\n")
