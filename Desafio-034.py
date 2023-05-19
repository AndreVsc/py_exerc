# Escreva um prgrama que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00 , calcule um aumento de 10%.Para inferiores ou iguais , o aumento de 15%.

salario = float(input('Qual salário atual do funcionário? : R$ '))
print()
if salario <= 1250 :
    print('O salário do funcionário será de R${:.2f}!'.format(salario*1.15))
elif salario >1250 :
    print('O salário do funcionário será de R${:.2f}!'.format(salario*1.1))