import random

opcoes = ['🍒', '💎', '7️⃣']
resultado = [random.choice(opcoes) for _ in range(3)]

print(f"Resultado: {' | '.join(resultado)}")

if resultado[0] == resultado[1] == resultado[2]:
    print("Ganhaste, parabéns.")
else:
    print("Perdeste, tenta novamente.")