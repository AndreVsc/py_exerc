#DESAFIO-005
# Faça um programa que leia um número inteiro e moste na tela seu sucessor e seu antecessor.

n = int(input('Qual o valor? '))
print()
print('Seu antescessor é {} \nO valor {} \nSeu sucessor é {}'.format((n-1),n,(n+1)))

#Resolução:

print()
n = int(input ('Digite um numero: '))
a = n - 1
s = n + 1
print()
print('Analizando o número {} \nSeu antecessor é {} e o sucessor é {}'.format(n,a,s))

#DESAFIO-006
# Crie um algoritmo que leia um número e mostre o seu dobro , triplo e  raiz quadrada.

print()
n = int(input('Digite um numero? '))
print()
print('Analizando o numero {} \nSeu dobro é {}, seu triplo é {} \nA raiz quadrada é {:.1f} '.format(n,(n*2),(n*3),n**(1/2)))

#Resolução:

print()
n = int(input('Digite um numero? '))
print()
print('O dobro de {} vale {}.'.format(n,(n*2)))
print('O triplo de {0} vale {1}\nA raiz quadrado de de {0} é igual a {2:.2f} .'.format(n,(n*3),pow(n,(1/2))))
print()

#DESAFIO-007
#  Desenvolva um prograna que leia as duas notas de um aluno , calcule e moste a sua média.(tomar cuidado com ordem de procedência).

print()
n1 = float(input('Qual a primeira nota do aluno? '))
n2 = float(input('A segunda nota do aluno? '))
print()
print('A media do Aluno é : {:.1f}'.format((n1+n2)/2))

#Resolução:

print()
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1+n2)/2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1,n2,media))
print()

#DESAFIO-008
# Escreva um prograna que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print()
m = float(input('Uma medida em metros? '))
print()
print('A medida {} metro(s) possuí: \n{} centimetros ou {} milimetros'.format(m,(m*100),(m*1000)))

#Resolução:

print()
m = float(input('Informe um valor em metros: '))
cm = m*100
ml = m*1000
print()
print('A media de {}m correspondente a {}cm ou {}ml'.format(m,cm,ml))

#Desafio//008

print()
mc = m*1000000
nnm = m*1000000000
km = m/1000
hc = m/100
dcm = m/10
dc = m*10


print('{} m tbm corresponde a :'.format(m))
print()
print('{} nanômetro \n{} micrômetro \n{} milímetros \n {} centímetros \n{} decímetros \n{} decametros \n{} hectometros \n{} kilometros'.format(nnm,mc,ml,cm,dc,dcm,hc,km))

#DESAFIO-009
# Faça um programa que leia um número inteiro qualquer e mostre a sua tabuada.

print ()
i = int(10)
n = int(input('Qual numero deseja calcular? '))
print ()
while (i > 0):
  m = (i*n)
  print(i,'x',n,'=',m)
  i=i-1 
print()

#Resolução:

num = int(input('Digite um numero para ver sua tabuada: '))
print('-'*12)
print('{} x {:2} = {}'.format(num,1, num*1))
print('-'*12)

#DESAFIO-010
# Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar.

print()
conta = float(100.00)
print('Voce tem atualmente R${:.2f} em sua conta '.format(conta))
print()
print('Em dolar atualmente vc tem R${:.2f} '.format(conta/3.27))

#Resolução:

print()
conta = float(input('Quanto dinheiro vc tem na sua conta? R$'))
print()
print('Com R${} voce pode comprar US${:.2f}'.format(conta,conta/3.27))

#DESAFIO-011
# Faça um programa que leia a altura e largura de uma parede em metros , calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinra pinta uma área de 2m².

print()
y = float(input('Altura da parede? '))
x = float(input('Largura da parede? '))
a = (x*y)
l = (a/2)
print()
print('A área da parede correspondente a {} m² \nA quantidade necessária em litros de tinta é {}L '.format(a,l))

#Resolução:

print()
larg = float(input('Largura da parede? '))
alt =  float(input('Altura da parede? '))
area = alt*larg
tinta = area/2
print()
print('sua parede ten dimensão de {}x{} e sua área é de {}m². '.format(larg,alt,area))
print('Para pontar essa parede, voce precisará de {}L de tinta. '.format(tinta))
print()

#DESAFIO-012
# Faça um algoritmo que leia um preço de um produto e mostre seu novo preço com 5% de desconto.

print()
preço = float(input('Qual o preco do produto? '))
print()
print('O valor do produto com 5% de desconto é R${} '.format(preço*0.95))

#Resolução: 

print()
preco = float(input('Qual é o preço do produto? R$')
novo = preco - (preco*5/100)
print('O pruduto que custava R${} , na promoção com desconto de 5% vai custar R${}. '.format(preco,novo))
print()

#DESAFIO-013
# Faca un algoritmo que leia o salário de um funcionário e mostre seu novo salario,com um aumento de 15%.(vou usar pra mim) obs: só multiplicar por 1.15 kk

print()
salario= float(input('Salário do funcionário? '))
print()
print('O salário do funcionário com o aumento sera {} tendo um aumento de {:.2f}'.format(salario*1.15,salario*0.15))

#Resolução:

salario = float(input('Qual o salário do funcionário? R$')
novo = salario + (salario*15/100)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${} '.format(salario,novo))