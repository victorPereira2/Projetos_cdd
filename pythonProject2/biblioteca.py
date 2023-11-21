def somar(n1,n2):
    resultado_1 = n1 + n2
    print(resultado_1)
def subtracao(n1,n2):
    resultado_2 = n1 - n2
    print(resultado_2)
def divisao(n1,n2):
    resultado_3 = n1 / n2
    print(resultado_3)
def multiplicacao(n1,n2):
    resultado_4 = n1 * n2
    print(resultado_4)
def exercicio_1(n):
    for i in (1,n+1):
        print(str(i)*i)
def exercicio_2(n):
    for i in range(1,n+1):
        for x in range(1,i+1):
            print(x,end=" ")
        print()
def produto(produto,qtd,valor):


    qtd_estoque = qtd * valor
    return (produto,qtd_estoque)

def argumento(a):
    entrada = ""
    if a >0:
        return "p"
    elif a <0:
        return "n"
    elif a ==0:
        return "z"

def adicao(*parametros):
    resultado =0
    for i in parametros:
        resultado=resultado+x
    return resultado

def texto2(a):
    cont=0
    for x in a:
        if x not in " ":
            cont+=1
    print(cont)

    for i in range(len(a)-1,-1)




def