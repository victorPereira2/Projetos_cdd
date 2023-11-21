from bibliotecaCRUD import *


while True:
    print("MENU:")
    print("1.Cadastrar Funcionários")
    print("2.Cadastrar Modalidades")
    print("3.Cadastrar Alunos")
    print("2.Cadastrar Personal")

    pergunta = input("Selecione a opção desejada: ")

    if escolha == "1":

        nome= input("Escreva seu nome: ")
        salario= int(input("Digite seu salário: "))
        cpf = int(input("Digite seu CPF: "))
        departamento = int(input("Digite seu departamento: "))
        filhos = input("Digite quantos filhos você tem: ")
        sql = "insert into func (nome, salario,cpf,departamento,filhos) values (%s,%s,$s,$s,$s)"
        data = (nome,salario,cpf,departamento,filhos)





