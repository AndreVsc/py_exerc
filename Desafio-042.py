# Refaça o DESAFIO 035 dos triângulos, acrescentando o 
# recurso de mostrar que tipo de triângulo será formado:
#
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

l1 = float(input('Digite o 1° lado : '))
l2 = float(input('Digite o 2° lado : '))
l3 = float(input('Digite o 3° lado : '))

print()

if l1<l2+l3 or l2<l1+l3 or l3<l1+l2 :
    if l1==l2==l3 :
        print('O triângulo é EQUILÁTERO. ')
    elif l1==l2 and l1!=l3 or l2==l3 and l2!=l3 or l3==l1 and l3!=l2 :
        print('O triangulo é ISÓCELES. ')
    elif l1!=l2 and  l2!=l3 and l1!=l3 :
        print('O triângulo é ESCALENO. ')
else:
    print('Não é possivel formar um triângulo. ')