# 1- crie um algoritmo em python que pergunte ao usuário quantos alunos tem
#na sala e criar um array, unidimensional(Vetor) com o nome de todos os alunos dasala
num_alunos = int(input("Quantos alunos há na sala? "))


lista_alunos = []

# Preenche o vetor com os nomes dos alunos
for i in range(num_alunos):
    # Pede o nome do aluno e adiciona ao vetor
    nome = input("Digite o nome do aluno {}: ".format(i + 1))
    lista_alunos.append(nome)

# Imprime o vetor com os nomes dos alunos
print("\nNomes dos alunos na sala:")
for nome in lista_alunos:
    print(nome)



# Arrays
qtd = int(input("Informe a quantidade de alunos presente em sala: "))
alunos = [" "] * qtd
e = [" "] * qtd

for i in range(qtd):
    alunos[i] = input(f"Informe o nome do aluno {i + 1}: ")

for t in range(qtd):
    print(f"{alunos[t]} está na posição {t}")