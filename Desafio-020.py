#DESAFIO
#O mesmo professor vai sortear a ordem de apresentação de trabalho dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem do sorteio.

from random import shuffle

alunos = []
i = 0
while i<=3:
  alunos.append(str(input ('Nome do aluno: ')).capitalize())
  i = i+1
shuffle(alunos)
print('A ordem dos alunos será : {}'.format(','.join(alunos)))

