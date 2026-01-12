# se for positivo print do 1 até ao max
# se for negativo print do max até ao 0

i = 0
maxi = int(input("Digite: "))

if maxi > 0:
    while i <= maxi:
        print(maxi)
        maxi -= 1
else:
    i = maxi
    while i <= 0:
        print(i)
        i += 1
