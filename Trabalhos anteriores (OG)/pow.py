base = int(input("Qual é a base?: "))
expoente = int(input("Qual é o expoente?: "))
potencia = 1
count = 1

while count <= expoente:
    potencia *= base
    count += 1
print(potencia)


