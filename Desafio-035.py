a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
print ()
if  a < b+c and b < c+a and c < b+a :
    print('É possivel fazer um triângulo')
else:
    print('Não é possível fazer um triângulo')