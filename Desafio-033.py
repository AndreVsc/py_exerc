# leia três numeros e mostre qual é o maior e qual o menor.
i = 0
maior = 0
menor = 0
while i<3:
    num = int(input('Digite um número : '))
    if num > maior:
        maior= num
    if menor==0 or num < menor:
        menor= num
    i= i+1
print('Maior numero: {} \nMenor numero: {}'.format(maior,menor))