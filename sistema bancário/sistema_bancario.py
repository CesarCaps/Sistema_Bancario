#parâmetros iniciais
saldo = valor_sacado = numero_saques = 0
limite_diario = 500
LIMITE_SAQUES = 3
extrato = []

while True:
    #cabeçalho
    print("=" * 100)
    print(f"{'SISTEMA BANCÁRIO':^100}")
    print("=" * 100)

    #menu principal
    menu = ['Depósito', 'Saque', 'Extrato', 'Encerrar']
    print("Menu Principal:")
    print(f"1 - {menu[0]}")
    print(f"2 - {menu[1]}")
    print(f"3 - {menu[2]}")
    print(f"0 - {menu[3]}")
    opcao = int(input("Selecione a Alternativa de sua escolha: "))

# DEPÓSITO
    if (opcao == 1):
        valor = float(input("informe o valor a ser depositado: R$"))
        if (valor < 0):
            print("Não é possível inserir valores negativos!")
        else:
            saldo += valor
            extrato.append(saldo)
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")

# SAQUE
    elif (opcao == 2):
        if (numero_saques == LIMITE_SAQUES):
               print("Limite diário de saque atingido!")
        else:
            valor = float(input("informe o valor a ser sacado: R$"))
            if (valor < 0):
                print("Valor inválido!")
            
            else:
                if (valor > 500):
                    print("Limite de saque de R$500,00 excedido!")
                elif(valor > saldo):
                    print("Saldo insuficiente!")
                else:
                    valor_sacado += valor
                    saldo -= valor
                    extrato.append(-valor)
                    numero_saques += 1
                    print(f"Saque de R${valor:.2f} realizado com sucesso!")

# EXTRATO
    elif(opcao == 3):
        print("exibindo histórico de entradas de saldo: ")
        print(extrato)
        print(f"Saldo total: R${saldo:.2f}")

        
# SAIR DO PROGRAMA
    elif(opcao == 0):
        break

# DEFAULT PADRÃO
    else:
        print("Opção inválida!")


