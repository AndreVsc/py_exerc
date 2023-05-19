# A Confederação Nacional de Natação precisa de um programa 
# que leia o ano de nascimento de um atleta e mostre sua 
# categoria, de acordo com a idade:
#
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

import datetime

data = datetime.date.today()
ano = data.year 

nasc = int(input('Em que ano você nasceu : '))
anv = str(input('Já fez aniversário este ano? (s/n) : ').upper())
if anv == 'S' :
   idade=ano-nasc
elif anv == 'N' :
   idade=(ano-nasc)-1
print()

if idade <= 9 :
    print('Atleta MIRIM')
elif idade <=14 :
    print('Atleta INFÂNTIL')
elif idade <=19 :
    print('Atleta JUNIOR')
elif idade <=25 :
    print('Atleta SÊNIOR')
elif idade > 25 :
    print('Atleta MASTER')
