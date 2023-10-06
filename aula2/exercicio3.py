time1 = input("Informe o nome do time1: ")
gols_time1 = int(input("Informe a quantidade de gols feitos pelo time1: "))

time2 = input("Informe o nome do time2: ")
gols_time2 = int(input("Informe a quantidade de gols feitos pelo time2: "))

if gols_time1 > gols_time2:
    print(f"{time1} venceu a partida por {gols_time1} X {gols_time2}!")
elif gols_time1 < gols_time2:
    print(f"{time2} venceu a partida por {gols_time2} X {gols_time1}!")
else:
    print(f"A partida terminou empatada por {gols_time1} X {gols_time2}")