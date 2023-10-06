dentro_intervalo = 0
fora_intervalo = 0
for i in range(10):
    n1 = int(input("Digite 10 valores: "))
    if n1 >= 10 and n1 <= 20:
        dentro_intervalo = dentro_intervalo + 1
fora_intervalo = 10 - dentro_intervalo
print(f"Quantidade de números dentro do intervalo: {dentro_intervalo}")
print(f"Quantidade de números fora do intervalo: {fora_intervalo}")




