#DESAFIO 3
#Crie um programa que leia dois numeros e mostre a soma entre eles.

num1 = int (input('Digite o \033[0;33mprimeiro\033[m valor: '))
num2 = int (input('Digite o \033[0;33msegundo\033[m valor: '))
soma = num1+num2
print()
print('A soma entre \033[0;33m{}\033[m e \033[0;33m{}\033[m é igual á \033[1;32m{}\033[m!'.format(num1,num2,soma))
print()

#DESAFIO 4
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.abs

x = input('Digite algo : ')

print()
print('O valor é do tipo primidtivo ',type(x))

print()
print('O valor é numérico? ',x.isnumeric())

print()
print('O valor é alfabético? ',x.isalpha())

print()
print('O valor é decimal? ',x.isdecimal())

print()
print('O valor é alfanumérico? ',x.isalnum())

print()
print('O valor possui todas as letras maiúsculas? ',x.isupper())

print()
print('O valor possui apenas letras minúsculas? ',x.islower())

print()
print('O valor possui apenas espaço? ',x.isspace())

print()
print('O valor é imprimível? ',x.isprintable())

print()
print('Todo o valor é contém caracteres ASCII? ',x.isascii())

print()
print('Todos os caracteres são dígitos? ',x.isdigit())

print()
print('Contém apenas letras alfanuméricas (az) e (0-9) ou sublinhados (_)? ',x.isidentifier())
