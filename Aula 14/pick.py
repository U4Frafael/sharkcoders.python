pergunta = input("Diga um país: ")
paises = ["Portugal", "Espanha", "China", "Russia", "Bangladesh", "India", "Alemanha"]
found = 0

for n in paises:
    if n == pergunta:
        found = 1
        print("País encontrado!")

if found == 0:
    print("País não encontrado.")