# Faça um programa que leia um número de 0 a 9999 
#e mostre na tela cada um dos digitos separados.(tentar por string e inteiros)
# Ex: digitar:187
#
# unidade: 7
# dezena: 8
# centena: 1

num1 = int(input('Me diga um numero de 0 a 9999 : '))
if num1<10000 and num1>=0:
    uni = num1%10 #unidade de qualquer numero
    dez = int(((num1-uni)/10)%10) # calculando dezena
    cem = int(((num1-((dez*10)+uni))/100)%10)
    uniM = int((num1-((cem*100)+(dez*10)+uni))/1000)
    print()
    print('Unidade : {}'.format(uni))
    print('Dezena  : {}'.format(dez))
    print('Centena : {}'.format(cem))
    print('Unidade de Milhar : {}'.format(uniM))
    print()
else:
    print()
    print('ERROR : Esse numero é maior que 9999 ')
    print()

    
num = input('Escreva um numero de 0 a 9999 : ')
if len(num)<4 or len(num)==0:
    while len(num)<4 :
        num = '0'+num
    print()
    print('Unidade : {}'.format(num[3]))
    print('Dezena  : {}'.format(num[2]))
    print('Centena : {}'.format(num[1]))
    print('Unidade de milhar : {}'.format(num[0]))
else: 
    print()
    print('ERROR : Esse numero é maior que 9999')
