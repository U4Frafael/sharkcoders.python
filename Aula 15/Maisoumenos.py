from random import randint

x = randint(1, 101)
lst = int(input("Insia um número: "))
tentativas = 0

while lst != x and lst < x:
    print(f'Número incorreto e menor. || Tentativa {tentativas}')
    tentativas += 1
    break