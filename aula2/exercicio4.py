litros_combustivel = float(input("Digite a quantidade em litros do combustível escolhido: "))
tipo_combustivel = input("Digite o tipo de combustível escolhido: G- Gasolina ou E- Etanol: ")
if tipo_combustivel=="g":
    print("O preço da gasolina está R$5,80 o litro, ")
    valor_pago_gasolina = litros_combustivel * 5.80
    print(f"O valor a ser pago é: {valor_pago_gasolina}")
elif tipo_combustivel=="e":

    print("O preço do etanol está R$4,90 o litro")
    valor_pago_etanol = litros_combustivel * 4.90
    print(f"O valor a ser pago é: {valor_pago_etanol}")
else:
    print("Erro")

