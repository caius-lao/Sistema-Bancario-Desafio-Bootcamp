from datetime import datetime

class Banco:
    MAX_SAQUE_DIA = 3
    MAX_SAQUE_VALOR = 500.0
    
    def __init__(self, saldo):
        self.saldo = saldo
        self.moviment = []
        self.cont_saque = 0
        
    def deposito(self, valor_deposito):
        if valor_deposito > 0:
            self.saldo += valor_deposito
            data = datetime.now().strftime("%d/%m/%Y %H:%M")
            self.moviment.append((data, "Depósito", valor_deposito))
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inserido inválido.")

    def saque(self, valor_saque):
        if self.cont_saque == self.MAX_SAQUE_DIA:
            print("Máximo de saques realizado para hoje.")
        elif valor_saque > self.MAX_SAQUE_VALOR:
            print("Valor solicitado excede R$500.00")
        elif valor_saque > self.saldo:
            print("Valor solicitado excede o saldo.")
        elif valor_saque > 0:
            self.saldo -= valor_saque
            data = datetime.now().strftime("%d/%m/%Y %H:%M")
            self.moviment.append((data, "Saque", valor_saque))
            print("Saque realizado com sucesso!")
            self.cont_saque += 1
        else:
            print("Valor inserido inválido.")
        
    def extrato(self):
        print("=================== EXTRATO ===================\n")
        if self.moviment == []:
            print("Não foram realizadas movimentações.")
        else:
            for i in range(len(self.moviment)):
                print(f"{self.moviment[i][0]} |{self.moviment[i][1]: ^10}| R$ {self.moviment[i][2]:.2f}\n")
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("===============================================")
