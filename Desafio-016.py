#DESAFIO
# Faca um programa que leia um numero do teclado qualquer e moste na tela sua porção inteira. Ex: 6.17 será 6.(math


from math import floor , trunc

num = float(input('digite um número qualquer: '))
print()
print('O numero {}, sua porção inteira corresponde á {}.'.format(num,floor(num))) # aredondad para baixo
print()

#Resolição-01:

num = float(input('Digite um valor: '))
print()
print('O numero digitado foi {} a parte inteira é {}'.format(num,trunc(num)))
print()

#Resolução-02:

num = float(input('Digite um valor: '))
print()
print('O nimero digitado foi {} a parte intera é {:0}.'.format(num,num))