#Faça um programa que leia uma frase e mostre:
# > Quantas vezes a letra "A" aparece na frase.
# > Em que lugar aparece a primeira vez.
# > Em que lugar aprece a última vez.

frase = input('Escreva uma frase : ').strip()
print()
frase = frase.upper()
print('Na frase a letra "a" se repete :',frase.count('A'))
print('A preimeira posiçao que ela aparece : ',1+frase.find('A'))
print('A ultima posição que ela aparece : ',1+frase.rfind('A'))