# Crie um programa que faça o computador jogar Jokenpô 
# contra você.

from random import randint

joken = ['PEDRA','PAPEL','TESOURA']

print('Vamos jogar jokenpô ')
print('[0] Pedra \n[1] Papel \n[2] Tesoura')
print()

jkp = randint(0,2)
ppt = int(input('Qual você escolhe? : '))
print()

if jkp == ppt :
    print('Empate! Ambos jogaram {}'.format(joken[ppt]))
elif ppt==0 and jkp==2 or ppt==1 and jkp==0 or ppt==2 and jkp==1 :
    print('Você venceu ! O computador jogou {}'.format(joken[jkp]))
elif ppt==0 and jkp==1 or ppt==1 and jkp==2 or ppt==2 and jkp==0 :
    print('Você perdeu ! O computador ganhou jogando {}'.format(joken[jkp]))
else:
    print('Valor inválido')
