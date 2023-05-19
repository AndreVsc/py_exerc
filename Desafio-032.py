#Faca um programa que leia um ano e mostre se é bissexto.
from datetime import date
ano = int(input('Digite um ano : '))
print()

if ano == 0 :
    ano = date.today().year
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print ('O ano de {} NÃO é BISSEXTO.'.format(ano))
print()
print("""O ano bissexto, aquele que é acrescentado um 
dia extra, ficando com 366 dias, um dia a 
mais do que os anos normais de 365 dias, 
ocorrendo a cada quatro anos. Isto é feito 
com o objetivo de manter o calendário anual 
ajustado com a translação da Terra e com os 
eventos sazonais relacionados às estações.""")
