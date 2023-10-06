#Para verificar se é par, usamos ( %2==0) ou seja, o número divisível por 2 com resto zero.
n1 = int(input("Escreva um número: "))
if n1 % 2 == 0:
    print("Seu número é par! ")
else:
    print("Seu número é ímpar!")