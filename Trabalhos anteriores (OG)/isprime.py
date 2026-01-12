num = int(input("Digite o número: "))
divisor = 2

while divisor < num:
    if num % divisor == 0:
        print(f"O número {num} não é primo")
        break
    divisor += 1
else:
    print(f'O número {num} é primo')