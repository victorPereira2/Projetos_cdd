from biblioteca import *
while True:


    funcao = str(input("Digite: \n\t1 - somar\n\t 2 - subtrair\n\t 3 - dividir\n\t 4- multiplicar\n\t S - SAIR\n\t"))
    if opcao not in "sS":
        n1 = float(input("Digite o valor de n1: "))
        n2 = float(input("Digite o valor de n2: "))

    if opcao in "sS":
        print("Programa finalizado!")
        break
    elif funcao == '1':
        somar(n1,n2)
    elif funcao == '2':
        subtracao(n1,n2)
    elif funcao == '3':
        divisao(n1,n2)
    elif funcao == '4':
        multiplicacao(n1,n2)

    else:
        print("Opção inválida!")




