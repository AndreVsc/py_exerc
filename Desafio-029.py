# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
# 80Km/h , mostre uma menssagem dizendo que ele foi multado .
# A multa vai custar R$7 a mais por cada Km acima do limite.

km = float(input('Qual a velocidade do carro? km'))
print()
if km > 80 :
    multa = (km-80)*7
    print('Parece que alguém está passando dos limites, sua multa será de R${:.2f} \nPor estar a {:.1f}Km/h '.format(multa,km))
print('Boa tarde! continue dirigindo em segurança.')