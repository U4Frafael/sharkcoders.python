num = int(input("Número: "))
cont = 1

while cont * cont <= num:
    if cont * cont == num:
        print(cont)
        break
    cont += 1

else:
    print(0)