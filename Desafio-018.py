#DESAFIO
# Faça um programa que leia um ângulo qualquer e leia na tela o valor do seno,cosseno e tangente desse angulo.

import math

ang = int(input('Me diga um angulo: '))
print('O valor da cosseno é {:.2f} \nO valor do seno é {:.2f} \nO valor do tangente é {:.2f}. '.format(math.cos(math.radians(ang)),math.sin(math.radians(ang)),math.tan(math.radians(ang))))
print()

