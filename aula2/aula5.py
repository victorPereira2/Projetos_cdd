#n = 0
#while n < 10:
#    n = n + 1
#    print(n)
###################3
#variavel = 0
#x = 1
#y = int(input("Digite quantas notas você vai lançar: "))
#while x <= y:
#    nota = float(input("Digite suas notas: "))
#    variavel = variavel + nota
#    #Realizando o loop com o contador:
#    x += 1
#media = variavel / y
#print(media)
######################



#resultado = 0
#n1 = int(input("Digite um valor para n1: "))
#n2 = int(input("Digite um valor para n2: "))
#while n2 == 0:
#    n2 = int(input("Digite novamente o valor n2: "))
#resultado = n2 / n1
#print(resultado)

###########################

#resultado = 0
#n1 = int(input("Digite um valor para n1: "))
#n2 = int(input("Digite um valor para n2: "))
#r = 1
#while n2 == 0:
#    n2 = int(input("Digite novamente o valor n2: "))
#    if r >= 5:
#        break
#    r +=1
#else:
#    resultado = n2 / n1
#    print(resultado)

##########################
#senha_correta = 'victor'
#tentativas = input("Digite sua senha: ")
#x = 1
#while tentativas != senha_correta:
#    tentativas = input("Digite novamente sua senha: ")
#    if x >= 2:
#        print("Número máximo de tentativas. Senha bloqueada! ")
#        break
#    x += 1
#else:
#    print("Senha correta")
###########################

senha_correta = 'victor'
tentativas = input("Digite sua senha: ")
x = 1
while tentativas != senha_correta:
    ## pode ser usada tambem print(f"restam {3 - x} tentativas")
    tentativas = input("Senha incorreta, digite novamente sua senha:  ")

    if x >=3 and tentativas != senha_correta:
        print("Número máximo de tentativas. Senha bloqueada! ")
        break
    x += 1

else:
    print("Login efetuado com sucesso!!")







