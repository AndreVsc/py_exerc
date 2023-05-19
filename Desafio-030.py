# Crie um programa que leia um numero e diga se ele é impar ou par

num = int(input('Me diga um numero : '))
print()
if num % 2 == 1 :
    print('O numero {} é IMPAR'.format(num))
else:
    print('O numero {} é PAR'.format(num))
