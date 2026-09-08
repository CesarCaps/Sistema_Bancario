from datetime import datetime
from interface.Interface import Cabecalho_cadastro_conta, Cabecalho_consulta_saldo, Cabecalho_depositar, Cabecalho_saque, Cabecalho_transferencia


class Conta:
    def __init__(self, tipo, cpf, numero_conta, saldo=0):
        self.tipo = tipo
        self.cpf = cpf
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.extrato = []

    def __str__(self):
        return f"Conta: {self.numero_conta}, CPF: {self.cpf}, Saldo: R${self.saldo:.2f}"
    
    def __repr__(self):
        return self.__str__()

def Cadastrar_conta():
    from Dados_iniciais.Dados import Contas_corrente, Contas_poupanca
    from classes.Extrato import Extrato
    Cabecalho_cadastro_conta()
    print("Cadastro de Conta")
    while True:
        tipo = input("Digite o tipo da conta (1-Corrente/2-Poupança): ").strip()
        if tipo in ["1", "2"]:
            if tipo == "1":
                tipo = "Corrente"
            else:
                tipo = "Poupança"
            break
        else:
            print("Tipo de conta inválido! Tente novamente.")

    cpf = input("Digite o CPF do cliente: ")
    numero_conta = input("Digite o número da conta: ")
    while True:
        try: #loop para impedir saldo inicial negativo ou inválido
            saldo = float(input("Digite o saldo inicial da conta: "))
            if saldo < 0:
                print("Saldo inicial não pode ser negativo! Tente novamente.")
            else:
                break
        except ValueError:
            print("Saldo inválido! Digite um número válido.")
    
    conta = Conta(tipo, cpf, numero_conta, saldo)
    conta.extrato.append(Extrato("Abertura de Conta", saldo, datetime.now().strftime("%d/%m/%Y %H:%M:%S"), saldo))
    
    
    if tipo == "Corrente":
        Contas_corrente.append(conta)

    else:
        Contas_poupanca.append(conta)
        
    return conta


def Consultar_saldo():
    from Dados_iniciais.Dados import Contas_corrente, Contas_poupanca
    Cabecalho_consulta_saldo()
    Conta = False #para verificar a existência de uma conta, se ao final permanecer como 'False' significa que a conta não existe.
    while True:
        tipo_conta = input("Digite o tipo da conta (1-Corrente/2-Poupança): ").strip()
        if tipo_conta == "1":
            numero_conta = input("Digite o número da conta para consultar o saldo: ")
            for conta in Contas_corrente:
                if conta.numero_conta == numero_conta:
                    print(f"Saldo atual da conta {conta.numero_conta}: R${conta.saldo:.2f}")
                    Conta = True
                    break
            break
        elif tipo_conta == "2":
            numero_conta = input("Digite o número da conta para consultar o saldo: ")
            for conta in Contas_poupanca:
                if conta.numero_conta == numero_conta:
                    print(f"Saldo atual da conta {conta.numero_conta}: R${conta.saldo:.2f}")
                    Conta = True
                    break
            break
        else:
            print("Tipo de conta inválido! Tente novamente.")
    if Conta == False:
        print("Conta inexistente! Tente novamente.")

def Realizar_deposito():
    from Dados_iniciais.Dados import Contas_corrente, Contas_poupanca
    from classes.Extrato import Extrato
    Cabecalho_depositar()
    Conta = False #para verificar a existência de uma conta, se ao final permanecer como 'False' significa que a conta não existe.
    while True:
        tipo_conta = input("Digite o tipo da conta (1-Corrente/2-Poupança): ").strip()
        if tipo_conta == "1":
            lista_alvo = Contas_corrente
            break
        elif tipo_conta == "2":
            lista_alvo = Contas_poupanca
            break
        else:
            print("Tipo de conta inválido! Tente novamente.")

    numero_conta = input("Digite o número da conta para realizar o depósito: ")
    for conta in lista_alvo:
        if conta.numero_conta == numero_conta:
            print(f"Saldo em conta: R${conta.saldo:.2f}")
            while True:
                try:
                    valor_deposito = float(input("Insira o valor do depósito: R$"))
                    if valor_deposito < 0:
                        print("O valor não pode ser negativo! Tente novamente.")
                    else:
                        break
                except ValueError:
                    print("Saldo inválido! Digite um número válido.")
            conta.saldo += valor_deposito
            print()
            print("Valor depositado com sucesso!")
            print(f"Saldo atual da conta {conta.numero_conta}: R${conta.saldo:.2f}")
            conta.extrato.append(Extrato(tipo="Depósito", valor=valor_deposito, data_hora=datetime.now().strftime("%d/%m/%Y %H:%M:%S"), saldo=conta.saldo))
            Conta = True
            break
        break    
    if Conta == False:
        print("Conta inexistente! Tente novamente.")        


def Realizar_saque():
    from Dados_iniciais.Dados import Contas_corrente, Contas_poupanca
    from classes.Extrato import Extrato
    Cabecalho_saque()
    Conta = False #para verificar a existência de uma conta, se ao final permanecer como 'False' significa que a conta não existe.

    while True:
        tipo_conta = input("Digite o tipo da conta (1-Corrente/2-Poupança): ").strip()
        if tipo_conta == "1":
            lista_alvo = Contas_corrente
            break
        elif tipo_conta == "2":
            lista_alvo = Contas_poupanca
            break
        else:
            print("Tipo de conta inválido! Tente novamente.")
            
    numero_conta = input("Digite o número da conta: ")
    for conta in lista_alvo:
        if conta.numero_conta == numero_conta:
            print(f"Saldo em conta: R${conta.saldo}")
            while True:
                try:
                    valor_saque = float(input("Insira o valor do saque: R$"))
                    if valor_saque < 0:
                        print("O valor não pode ser negativo! Tente novamente.")
                    elif valor_saque > conta.saldo:
                        print("Valor inválido!")
                    else:
                        break
                except ValueError:
                    print("Saldo inválido! Digite um número válido.")
            conta.saldo -= valor_saque
            print()
            print("Valor sacado com sucesso!")
            print(f"Saldo atual da conta {conta.numero_conta}: R${conta.saldo:.2f}")
            conta.extrato.append(Extrato(tipo="Saque", valor=valor_saque, data_hora=datetime.now().strftime("%d/%m/%Y %H:%M:%S"), saldo=conta.saldo))
            Conta = True
            break
        break
    
    if Conta == False:
        print("Conta inexistente! Tente novamente.")

def transferencia():
    from Dados_iniciais.Dados import Contas_corrente, Contas_poupanca
    from classes.Extrato import Extrato
    Cabecalho_transferencia()
    Conta_corrente = False
    Conta_poupanca = False
    while True:
        tipo_conta = input("Digite o tipo de transferência (1-Corrente - Poupança / 2-Poupança - Corrente): ").strip()
        if tipo_conta == "1":
            numero_conta = input("Digite o número da conta: ")
            for conta_cor in Contas_corrente:
                if conta_cor.numero_conta == numero_conta:
                    Conta_corrente = True
                    for conta_pou in Contas_poupanca:
                        if conta_pou.numero_conta == numero_conta:
                            Conta_poupanca = True
                            while True:
                                try:
                                    valor_transferencia = float(input("digite o valor da transferência: R$"))
                                    if valor_transferencia > conta_cor.saldo:
                                        print("Saldo insuficiente!")
                                    elif valor_transferencia < 0:
                                        print("Valor não pode ser negativo! Tente novamente.")
                                    else:
                                        break
                                except ValueError:
                                    print("Saldo inválido! Digite um número válido.")
                            conta_cor.saldo -= valor_transferencia
                            conta_pou.saldo += valor_transferencia
                            conta_cor.extrato.append(Extrato(tipo="Transferência", valor=-valor_transferencia, data_hora=datetime.now().strftime("%d/%m/%Y %H:%M:%S"), saldo=conta_cor.saldo))
                            conta_pou.extrato.append(Extrato(tipo="Transferência", valor=valor_transferencia, data_hora=datetime.now().strftime("%d/%m/%Y %H:%M:%S"), saldo=conta_pou.saldo))
                            print("Transferencia realizada com sucesso!")
                            print()
                            print("Saldo atual:")
                            print(f"Conta corrente: R${conta_cor.saldo}")
                            print(f"Conta poupança: R${conta_pou.saldo}")
                            break
                        if Conta_poupanca == False:
                            print("Conta poupança inexistente!")
                    if Conta_corrente == False:
                        print("Conta corrente inexistente!")
                        break
            if Conta_corrente == False or Conta_poupanca == False:
                print("Conta inexistente!")
            break
        
        elif tipo_conta == "2":
            numero_conta = input("Digite o número da conta: ")
            for conta_pou in Contas_poupanca:
                if conta_pou.numero_conta == numero_conta:
                    Conta_poupanca = True
                    for conta_cor in Contas_corrente:
                        if conta_cor.numero_conta == numero_conta:
                            Conta_corrente = True
                            while True:
                                try:
                                    valor_transferencia = float(input("digite o valor da transferência: R$"))
                                    if valor_transferencia > conta_pou.saldo:
                                        print("Saldo insuficiente!")
                                    elif valor_transferencia < 0:
                                        print("Valor não pode ser negativo! Tente novamente.")
                                    else:
                                        break
                                except ValueError:
                                    print("Saldo inválido! Digite um número válido.")
                            conta_cor.saldo += valor_transferencia
                            conta_pou.saldo -= valor_transferencia
                            conta_cor.extrato.append(Extrato(tipo="Transferência", valor=valor_transferencia, data_hora=datetime.now().strftime("%d/%m/%Y %H:%M:%S"), saldo=conta_cor.saldo))
                            conta_pou.extrato.append(Extrato(tipo="Transferência", valor=-valor_transferencia, data_hora=datetime.now().strftime("%d/%m/%Y %H:%M:%S"), saldo=conta_pou.saldo))
                            print("Transferencia realizada com sucesso!")
                            print()
                            print("Saldo atual:")
                            print(f"Conta corrente: R${conta_cor.saldo}")
                            print(f"Conta poupança: R${conta_pou.saldo}")
                            break
                        if Conta_corrente == False:
                            print("Conta corrente inexistente!")
                            break
                    if Conta_poupanca == False:
                        print("Conta poupança inexistente!")
                    
            if Conta_corrente == False or Conta_poupanca == False:
                print("Conta inexistente!")
            break

        else:
            print("Tipo de conta inválido! Tente novamente.")

        
def Emitir_extrato():
    from interface.Interface import Cabecalho_extrato
    from Dados_iniciais.Dados import Contas_corrente, Contas_poupanca, Clientes
    Cabecalho_extrato()
    while True:
        tipo_conta = str(input("1-Conta Corrente / 2-Conta Poupança: "))
        if tipo_conta == "1":
            lista_alvo = Contas_corrente
            break
        elif tipo_conta == "2":
            lista_alvo = Contas_poupanca
            break
        else:
            print("Tipo inválido!")

    conta_ = input("Informe o número da conta (xxxx-x): ")
    for conta in lista_alvo:
        encontrada = False
        if conta_ == conta.numero_conta:
            encontrada = True
            conta_alvo = conta
            break

    if encontrada == False:
        print("Conta não encontrada!")
        return

    else:
        print("Conta encontrada!")
        if not conta_alvo.extrato:
            print("Não há transações para exibir.")
            return
        else:
            for transacao in conta_alvo.extrato:
                print(f"{"="*100}\nData/Hora: {transacao.data_hora} \n Tipo: {transacao.tipo} \n Valor: R${transacao.valor:.2f} \n Saldo: R${transacao.saldo:.2f}")