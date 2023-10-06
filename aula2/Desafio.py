hora_entrada_1 = int(input("Digite o valor da hora de entrada: "))
minuto_entrada_1 = int(input("Digite o valor dos minutos1"))
hora_entrada_2 = int(input("Digite o valor da hora2: "))
minuto_entrada_2 = int(input("Digite o valor dos minutos2: "))
hora_final = hora_entrada_1 + hora_entrada_2
minuto_final = minuto_entrada_1 + minuto_entrada_2
#print(f"entrada01 {hora_entrada_1}:{minuto_entrada_1} e entrada02 {hora_entrada_2}:{minuto_entrada_2}")

if hora_final == 13:
    hora_final == 1
if hora_final == 14:
    hora_final == 2
if hora_final == 15:
    hora_final == 3
if hora_final == 16:
    hora_final == 4
if hora_final == 17:
    hora_final == 5
if hora_final == 18:
    hora_final == 6
if hora_final == 19:
    hora_final == 7
if hora_final == 20:
    hora_final == 8
if hora_final == 21:
    hora_final == 9
if hora_final == 22:
    hora_final == 10
if hora_final == 23:
    hora_final == 11
if hora_final == 24:
    hora_final == 0
print(f"{hora_final}:{minuto_final}")