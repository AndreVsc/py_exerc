# Elabore um programa que calcule o valor a ser pago por 
# um produto, considerando o seu preço normal e condição 
# de pagamento:
#
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

preco=float(input('Qual o preço do produto? : R$ '))
print()
print('Qual será a forma de pagamento? : ')
print('[1] Á vistá PIX 10% de desconto')
print('[2] Á vistá cartão 5% de desconto ')
print('[3] 2x sem juros no cartão ')
print('[4] 3x ou mais 20% de juros')
print()
forma = int(input('Digite o número da forma de pagamento : '))
print()

if forma==1 :
    preco=preco*0.9
    print('O valor do produto é R${:.2f}'.format(preco))
elif forma==2 :
    preco=preco*0.95
    print('O valor do produto é R${:.2f}'.format(preco))
elif forma==3 :
    print('O valor será 2x de R${} '.formar(preco/2))
elif forma==4 :
    vez=int(input('Quantas vezes? : '))
    preco=preco*1.2/vez
    print()
    print('O valor será {}x de R${:.2f}'.format(vez,preco))
else:
    print('Valor inválido')