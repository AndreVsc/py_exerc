# Escreva um programa em Python que leia um número inteiro 
# qualquer e peça para o usuário escolher qual será a base de 
# conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número : ')) 
print()
print('[1] binário \n[2] octal \n[3] hexadecimal \n')
boh = int(input('Escolha : '))
print()
if boh == 1 :
    binario = str(format(num,"b")).zfill(8)
    print('Em binário {} ficaria : {}'.format(num,binario))
elif boh == 2 :
    print('Em octal {} ficaria : {}'.format(num,oct(num)))
elif boh  == 3 :
   print('Em hexadecimal {} ficaria : {}'.format(num,hex(num)))
else:
    print('Valor invalido')
