# Crie um programa que leia o nome de ua cidade 
# e diga se ela COMEÇA ou não com "SANTO".

cidade = input('Digite o nome de uma cidade : ').strip()
cidade = cidade.upper().split()
print('SANTO' in cidade[0])

#resolução
 
print()
cid = input('Digite o nome de uma cidade : ').strip()
print(cid[:5].upper() == 'SANTO')