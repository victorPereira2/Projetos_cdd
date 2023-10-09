print("Game: Pedra, Papel e Tesoura, vamos começar!")

opcoes = ["pedra", "papel", "tesoura"]

while True:
    
    nome_jogador1 = input("Digite o nome do Jogador 1: ")
    nome_jogador2 = input("Digite o nome do Jogador 2: ")

    while True:
        escolha_jogador1 = input(f"{nome_jogador1}, escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ")

        if escolha_jogador1 == "sair":
            print("Até logo!")
            exit()

        if escolha_jogador1.lower() not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue

        escolha_jogador2 = input(f"{nome_jogador2}, escolha pedra, papel ou tesoura: ")

        if escolha_jogador2.lower() not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue

        print(f"{nome_jogador1} escolheu: {escolha_jogador1}")
        print(f"{nome_jogador2} escolheu: {escolha_jogador2}")

        if escolha_jogador1.lower() == escolha_jogador2.lower():
            print("Empate!")
        elif (escolha_jogador1 == "pedra" and escolha_jogador2 == "tesoura") or \
             (escolha_jogador1 == "papel" and escolha_jogador2 == "pedra") or \
             (escolha_jogador1 == "tesoura" and escolha_jogador2 == "papel"):
            print(f"Parabéns {nome_jogador1}, você venceu!")
        else:
            print(f"Parabéns {nome_jogador2}, você venceu!")

        
        jogar_novamente = input("Quer jogar novamente? (sim/não): ").lower()
        if jogar_novamente != "sim":
            print("Até logo!")
            exit()
        else:
            break
