atual = int(input('Digite a sua velocidade atual: '))
limite = int(input('Digite o limite de velocidade: '))

if atual > limite:
    print(f'Velocidade atual é: {atual}')
    print(f'Limite de velocidade é: {limite}')
    print(f'Excesso de velocidade foi de: {atual - limite}')
    print(f'Terá que pagar uma multa de {80 + (atual - limite)*2} euros.')

else:
    print("Limite de Velocidade respeitado, boa viagem :)" )
