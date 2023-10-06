#for i in range (de onde começa; até onde vai; de tanto em tanto)
#for i in range(1,11,2):
##(end=" " -->executa a a saída na vertical
#    print(i, end=" ")
#for e in range(8,0,-2):
#    print(e, end=" ")
#for i in range(101,111,1):
#   print(i, end=" ")
#n1 = int(input("Digite um número: "))
#for n1 in range(1,n1+1):
#    print(n1)

#Contador de números negativos:
soma = 0
cont = 0
positivos = 0
for i in range(0,11):
    n1 = int(input("Digite um número: "))
    if n1<0:
        cont = cont + 1

        print(n1)
        soma = soma + n1
        positivos = 10 - cont
print(soma)
print(f"Quantidade de números negativos: {cont}")

print(positivos)







