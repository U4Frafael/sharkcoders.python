from time import sleep

num = int(input("Insira um número: "))
while num != 0:
    print(num)
    num -= 1
    sleep(1)