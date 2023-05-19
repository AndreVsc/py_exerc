# Crie um programa que leia o nome de uma pessoa e diga 
# se ela tem "SILVA" no nome. (qualquer lugar do nome)

cidade = str(input('Digite o nome de uma cidade : ')).strip()
cidade = cidade.upper()
print('SILVA' in cidade)