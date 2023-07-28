from sistema_banco import Banco

class Menu:
    banco = Banco()
    menu = """
    Operações:
    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair

    => """
    
    def main(self):
        while True:
            op = input(self.menu)
            match op:
                case 'd':
                    self.banco.deposito(float(input("Insira o valor para depósito: ")))
                case 's':
                    self.banco.saque(float(input("Insira o valor para saque: ")))
                case 'e':
                    self.banco.extrato()
                case 'q':
                    break
                case _:
                    print("Opção inválida!")
