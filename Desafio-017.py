#DESAFIO
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule o comprimento da hipotenusa.

import math

op = float(input('Qual o tamanho do cateto oposto? '))
ad = float(input('Qual o tamanho do cateto adjacente? '))
print ()
h = (pow(op,2)+pow(ad,2))**(1/2)
print('O resultado da hipotenusa é {:.2f}'.format(h))
print()

#Resolução

op = float(input(('Comprimento do cateto oposto? ')))
ad = float(input('Comprimento do cateto adjacente? '))
print()
hi = math.hypot(op,ad)
print('A hipotenusa vai medir: {:.2f} '.format(hi))

