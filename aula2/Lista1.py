#6 questão:
# n1 = int(input("Digite um número: "))
# if n1 > 10:
#     print("Número maior que 10!!")
# elif n1 < 10:
#     print("O número não é maior que 10!!")
# else:
#     print("Seu número é 10!!")

# #7 questão:
# resposta = 's'
# while resposta == 'S' or resposta == 's' :
#     base = float(input("Digite o valor da base do triângulo: "))
#     while base <=0:
#         base = float(input("Número inválido, digite um valor maior que 0 na base do triângulo: "))
#     altura = float(input("Digite a altura do triângulo: "))
#     while altura <=0:
#         altura = float(input("Número inválido, digite um valor maior que 0 na altura do triângulo: "))
#     area = (base * altura)/2
#     print(f"A área do triângulo é: {area} ")
#     resposta = input("Deseja fazer outra operação? Digite S para repetir ou Não para encerrar!!: ")

# # 8 questão:
# cont = 0
# nota = 0
# media = 0
# qtd_notas = int(input("Digite a quantidade de notas: "))
#
# for i in range(qtd_notas):
#     nota = float(input("Digite as notas: "))
#     cont = cont + nota
# media = cont / qtd_notas
# print(f"Sua media é: {media}")

# 9 questão:
#pedir dois numeros e pedir a subtração do maior para o menor
#10: nao permitir que numeros iguais façam subtração
# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o segundo número: "))
# sub = 0
# if n1 > n2:
#     sub = n1 - n2
# elif n2 > n1:
#     sub = n2 - n1
# print(sub)
#
# #else:
# #print("Não permitido números iguais!!")
# sucessor = 0
# antecessor=0
# decisao = 0
# num = int(input("Digite um número: "))
# decisao = input("Digite 1 para antecessor, 2 para sucessor e 3 para sair do programa: ")
# while decisao == 1:
#     antecessor = num - 1
#     print(antecessor)
# while decisao == 2:
#     sucessor = num + 1
#     print(sucessor)
# elif decisao == 3:
#     print("Fim do programa!! ")
#corrigindo a de cima:
# while True:
#     numero =int(input("Digite um número: "))
#     opacao = int(input("Digite a opcao:\n "
#                        "1 para antecessor \n"
#                        "2 para sucessor \n"))
#     if opcao ==1:
#         print(numero-1)
#     elif opcao ==2:
#         print(numero+1)
#     else:
#         break

#11.
anos = int(input("Informe sua idade (Anos): "))
meses = int(input("Informe sua idade (Meses): "))
dias = int(input("Informe sua idade (Dias): "))

idade_dias = anos * 365 + meses * 30 + dias

print(f"Você viveu {idade_dias} dias.")






#8 questão


