# Desenvolva um programa que pergunte a distancia da viagem  em Km . caucule o preço da passagem
# cobrando R$0,50 por viagens até 200Km e R$0,45 por viagem mais longas.

km = int(input('Quantos Km a viagem percorreu? :  '))
print()
if km <= 200 :
    passagem = km * 0.5
else:
    print('Está viagem possui R$0,05 de desconto por Km!')
    passagem = km * 0.45
print('A passagem ficou por R${:.2f} pelos {}Km.'.format(passagem,km))
