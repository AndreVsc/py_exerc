# Crie um programa que leia duas notas de um aluno e calcule
# sua média, mostrando uma mensagem no final, de acordo 
# com a média atingida:
#
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

not1 = float(input('Qual a primeira nota do aluno : '))
not2 = float(input('Qual a segunda nota do aluno : '))
media = (not1+not2)/2
print()
if media < 5:
    print('O aluno foi REPROVADO')
elif media == 5 or media < 6:
    print('O aluno está de RECUPERAÇÃO')
elif media >= 6:
    print('O aluno foi APROVADO')