# Crie um programa que leia o nome de uma pessoa e moste:
# > O nome com todas as letras maiúsculas
# > O nome com todas as letras minúsculas
# > Quantas letras ao todo (sem considerar espaços)
# > Quantas letras tem o primeiro nome

nome = input('Qual seu nome completo? : ')
print()
print('Seu nome em maiúsculo é : ',nome.upper())
print('Seu nome em minúsculo é : ',nome.lower())
print('Seu nome possui : ',len(nome)-nome.count(' '),' letra(s)')
nome = nome.split()
print('Seu primeiro nome tem :',len(nome[0]),' letra(s)')

#resolução

print()
nome = input('Digite seu nome completo : ')
print('Analizando seu nome...')
print('Seu nome em maiúsculo é : ',nome.upper())
print('Seu nome em minúsculo é : ',nome.lower())
print('Seu nome possui {} letras '.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

