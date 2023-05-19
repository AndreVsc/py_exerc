# Desenvolva uma lógica que leia o peso e a altura de uma 
# pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
# seu status, de acordo com a tabela abaixo:
#
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

kg = float(input('Peso(kg) : '))
a = int(input('Aultra(cm) : '))

print()

a = a/100
imc = kg / (a**2)

print('Seu IMC é de {:.0f} '.format(imc))#

if imc<18.5 :
    print('Você está abaixo do peso')
elif imc>=18.5 and imc<25 :
    print('Voce tem um peso saudável ')
elif imc>=25 and imc<30 :
    print('Você possui sobrepreso')
elif imc>=30 and imc<40 :
    print('Você possui obesidade')
elif imc>40 :
    print('Você possui obesidade mórbida')
