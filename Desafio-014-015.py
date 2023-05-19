# Crie um programa que coverta unidade de calor de C° para F° . Sendo que 1° Celsius está para 33.8° grals fahrenheit.

Celsius = float(input('Informe a temperatura em C°: '))
ConF = (Celsius*(9/5)+32)
print()
print('{}° Celcius equivale a {}° Fahrenheit'.format(Celsius,ConF))

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelo qual ele foi alugado . Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

print()
dias = int(input('Quantos dias o cliente ficou com o carro? '))
km = float(input ('Quantos Km foram rodados? Km '))
alg = (dias*60) + (km*0.15)
print('O cliente passou {} dia(s) com o carro e rodou {} Km. Logo sua conta ficou de R${:.2f}'.format(dias,km,alg))