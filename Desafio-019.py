#DESAFIO
# Um professor quer sortear um dos seus alunos para apagar o quadro. faca um programa que ajude ele , lendo o nome deles e escrevendo o nome do escolido na tela.

from random import randint,choice
alunos = []
i=0
x = randint(0,3)
while i<4 :
  alunos.append(input('Nome do Aluno: '))
  i=i+1
print()
print('O aluno escolhido foi {} '.format(alunos[x]))
y = choice(alunos)
print()
print('O aluno escolido foi: {}'.format(y))