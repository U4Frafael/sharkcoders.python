import random
import time

dinheiro = 1000

def saldo():
    print(f'Saldo Atual: {dinheiro}')
    
    valor_input = input("Valor da aposta (ou '0' para sair): ")
    if valor_input == "0":
        exit()
    return int(valor_input)
    
def slot(valor):
    global dinheiro
    opcoes = ['🍒', '💎', '7️⃣']
    

    print("A girar...", end=" ")
    for _ in range(15):
        reels_fake = [random.choice(opcoes) for _ in range(3)]
        print(f" {' | '.join(reels_fake)} ", end="\r")
        time.sleep(0.25)   # mais lento


    resultado = [random.choice(opcoes) for _ in range(3)]
    print(f"Resultado: {' | '.join(resultado)} \n")
 
    if resultado[0] == resultado[1] == resultado[2]:
        print("Ganhaste, parabéns!\n")
        dinheiro += valor
    else:
        print("Perdeste, tenta novamente.\n")
        dinheiro -= valor

while True:
    try:
        valor = saldo()
        slot(valor)
    except ValueError:
        print("Por favor, insira um número válido.\n")
