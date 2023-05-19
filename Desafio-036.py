# Escreva um programa para aprovar o empréstimo bancário para
# a compra de uma casa. Pergunte o valor da casa, o salário 
# do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário 
# ou então o empréstimo será negado.


# prestação < 0.30*salario
# mes = anos*12
# prestação a pagar = meses/valor da casa

salario = float(input('Qual seu salário mensal? : '))
casa = float(input('Qual o valor da casa? : '))
anos = int(input('Em quantos anos pretente financer prestação? : '))
meses = anos*12
prestacao =  (casa/meses)
print()
if prestacao < salario*0.30 :
    print('\033[0;32mSeu imprestimo foi APROVADO!\033[m')
    print('O valor da prestação por mês será de R${:.2f} durante {} anos. '.format(prestacao, anos))
else:
    print('\033[0;31mSeu imprestimo foi RECUSADO!\033[m')
    print('O valor da casa exede 30% do salário mesal mas condições proprostas')
