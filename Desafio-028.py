# Escreva um programa que faça o computador "pensar" em numero de 0 a 5 
# e peça ao úsuario tentar descobrir qual foi o numero escolhido pelo computador.
# O programa deve dizer se o usuario venceu ou pedeu.

from random import randint

numImg = randint(0,5)
num = int(input("Pensei em um numero entre 0 e 5! vc consegue adivinhar? : "))
print()
if num == numImg :
    print('Você ganhou , PARABÉNS!')
else:
    print('Você perdeu , a resposta era {} !'.format(numImg))


#resolução

from time import sleep

computador = randint(0,5) # Numero ale. de 0 a 5.
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print ('PROCESSANDO...')
sleep(2)
if jogador == computador :
    print('PARÁBENS! Voce conseguiu acertar.')
else:
    print('GANHEI! o numero que eu tinha pensado era {}.'.format(computador))