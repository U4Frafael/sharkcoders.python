nota = int(input("Qual foi a nota?: "))

if nota < 0 or nota > 100:
    x = f'Nota inválida. (Nota: {nota})'
elif nota < 25:
    x = f'Muito Insuficiente (Nota: {nota})'
elif nota < 50:
    x = f'Insuficiente (Nota: {nota})'
elif nota < 70:
    x = f'Suficiente (Nota: {nota})'
elif nota < 90:
    x = f'Bom (Nota: {nota})'
else:
    x = f'Muito bom (Nota: {nota})'
print(x)