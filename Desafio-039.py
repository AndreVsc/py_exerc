# Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento. Seu programa também 
# deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

data = datetime.date.today()
dia = data.day
mes = data.month
ano = data.year

nasc = int(input('Qual seu ano de nascimento : '))
anv  = str(input('Fez aniversário esse ano (s/n) : ').upper)
if anv == 'S' :
    idade = ano-nasc
else:
    idade = ano-nasc-1
print()
if idade == 18 :
    print('Você tem que se alistar nesse ano ! ')
elif idade < 18 :
    faltam = 18 - idade
    print('Você ainda não precisa se aliastar , faltam {} ano(s)'.format(faltam))
elif idade > 18 :
    atraso = idade - 18
    print('Você já devia ter se alistado, está atrasado {} ano(s)'.format(atraso))
else:
    print('Idade inavlida ')