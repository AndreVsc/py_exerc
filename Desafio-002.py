#Crie um script que leia o nome de uma pessoa e escreva uma mensagem de boas-vindas.

nome = input('Qual seu nome? ')
print('Seja bem vindo '+nome+'! É um prazer em conhecer-te')
print()

# Resolução:

nome = input('Qual seu nome: ')
print('É um prazer te conhecer\033[1;32m{}\033[m!'.format(nome)) #format substituirá as '{}' dentro da frase com a variavel dentro de seus parentes.