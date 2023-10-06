nota1 = float(input("Digite a nota1: "))
nota2 = float(input("Digite a nota2: "))
nota3 = float(input("Digite a nota3: "))
if nota1 < 0 or nota1 > 10:
    print("Erro!")
elif nota2 < 0 or nota2 >10:
        print("Erro!")
elif nota3 < 0 or nota3 >10:
            print("Erro!")
else:
    media = (nota1 + nota2 + nota3) / 3

    if media <7:
        if media < 4:
            print(f"Sua média é:{media}, Infelizmente você foi reprovado!!")
        else:
            print(f"Sua média é :{media:.2f}, Infelizmente você está na recuperação!!")
    else:
        print(f"Sua média é: {media:.2f}, Parabéns, você foi aprovado!!")
