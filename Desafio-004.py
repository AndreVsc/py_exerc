# "+" Soma
# "-" Subtração
# "/" Divisão
# "*" Multiplicação
# "**" Potência
# "//" Resultado da Inteira
# "%" Resto da Divisão

#   Ordem de Precedência
# 1° ()
# 2° **
# 3° *  /  //  %
# 4° +  -

print(5+3*2)  # 5+3*2 = 5+6 = 11
print(3*5+4**2) # 3*5+4**2 = 3*5+16 = 15+16 = 31
print(3*(5+4)**2) # 3(5+4)**2 = 3*9**2 = 3*81 = 243

# Para calcular raiz quadrada apenas realize uma potência com um numero fracinal como expoente dento de parentes.

print()
print(81**(1/2)) # 49**1/2 = √49 = 7
print(27**(1/3)) # 27**1/3 = ³√27 = 3

# Sempre que ultilizado o "//" para divisa o resultado sera inteiro.

print()
print('5//2 = ',5//2) # 5/2 = 2.5 // = 2
print('3//4 = ',3//4) # 3/4 = 0.75 // = 0

# Quando ultilizarmos o "%" queremos o resto da divisão.


print()
print('Resto de 2/2 = {}'.format(2%2))
print('Resto de 10/3 = {}'.format(10%3))
print('Resto de 7/2 = ',7%2)

print()
print('a'+'a') #A soma de duas strings resulta em "aa"
print('a'*5) # A soma entre string e inteiros nao existe mas a multiplicação sim 

print()
nome = input('Qual seu nome? ')  # Pergunta insere valor na vareavel 
print()
print('Seja bem vindo, {:20} '.format(nome)) # Adiciona espaços na formatação da vareavel, fazendo possuir 20 caracteres.

print()
print('Seja bem vindo, {:>20} '.format(nome)) # Adiciona a vareavel 20 caracteres a direta.

print()
print('Seja bem vindo, {:<20}'.format(nome)) #  Adiciona a vareavel 20 caracteres a esquerda.

print()
print('Seja bem vindo,  {:^20}'.format(nome)) # Centraliza o nome em relacao a quantidade de caracteres

print()
print('Seja bem vindo, {:=^20}'.format(nome)) # Centraliza o valor e adiciona o sinal "=" nos restantes 

print()
n1 = int(input('Qual o primeiro número? '))
n2 = int(input('Qual o segundo? '))
print('A soma é {}'.format(n1+n2)) #Soma direto sem o uso preciso repetiivo.
s = n1 + n2
su = n1 - n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
e = n1 ** n2

print()
print('Entre {} e {} soma é {}, subtração é {} \nA divisão {:.2f} sobrando {} e a potência {}'.format(n1,n2,s,su,d,di,e))

