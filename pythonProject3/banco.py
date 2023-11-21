class conta_bancaria:
    def __init__(self):
        self.numero_conta = "54467"
        self.saldo_conta = 0
        self.nome_titular = "Victor"
        self.tipo_conta = "Corrente"
        self.status_conta = True
        self.limite = 0

    def depositar(self):
        if self.status_conta == True:
            valor = float(input("Informe o valor a ser depositado: "))
            valor = self.saldo_conta
        else:
            print("Conta inativa. Procure o SAC do seu banco!")

    def sacar(self):
        if self.status_conta == True and self.saldo_conta > 0:
            valor_saque = float(input("Informe o valor a ser sacado: "))
            valor_saque -= self.saldo_conta
        elif self.saldo_conta ==0:
            print("Saldo insuficiente!")

        elif self.status_conta == False:
            print("Conta Desativada, procure o Banco!")

    def ativarconta(self):
        if self.status_conta == False:
            self.status_conta = True
            print("Conta Ativada!")
        else:
            print("Conta já Ativada!")

    def desativarconta(self):
        if self.status_conta == True:
            self.status_conta = False
            print("Conta desativada!")
        else:
            print("Conta já desativada!")

    def verificarsaldo(self):
        if self.status_conta == True:
            print(f"Seu Saldo é de : {self.saldo_conta}")
        else:
            print("Conta desativada!")


class Animal():
    def __init__(self, nome, cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(f" O {self.nome} foi comer...")
    def EmiteSom(self):
        print(f"O {self.nome} está emitindo som...")
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def EmiteSom(self):
        print(f"O {self.nome} está miando...")
    def comer(self):
        print(f" O {self.nome} foi comer...")
class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)
    def EmiteSom(self):
        print(f"O {self.nome} está latindo...")
    def comer(self):
        print(f" O {self.nome} foi comer...")
class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)
    def EmiteSom(self):
        print(f"O {self.nome} está pulando...")
    def comer(self):
        print(f" O {self.nome} foi comer...")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)
    def EmiteSom(self):
        print(f"O {self.nome} está mugindo...")
    def comer(self):
        print(f" O {self.nome} foi comer...")