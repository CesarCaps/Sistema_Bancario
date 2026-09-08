import classes.Conta as Conta
import classes.Cliente as Cliente
import classes.Extrato as Extrato
import Dados_iniciais.Dados as Dados
from interface.Interface import Cabecalho_main

funcoes = ("Sair", "Cadastrar Cliente", "Cadastrar Conta", "Consultar Saldo", "Realizar Depósito", "Realizar Saque", "Transferir Valor", "Listar Clientes", "Listar Contas", "Extrato")

def main():
    while True:
        Cabecalho_main()

        for c in range(len(funcoes)): # para cada função, exibe a opção
            if c == 0:
                print(f"{c}. {funcoes[c]}")
            else:
                print(f"{c}. {funcoes[c]}")

        print() #cria uma linha em branco para separar o menu da entrada do usuário
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            break
        elif opcao == "1":
            try:
                Cliente.Cadastrar_cliente()
                print("\n Cliente cadastrado com sucesso!".center(100))
            except Exception as e:
                print(f"Erro: {e}")
        elif opcao == "2":
            try:
                Conta.Cadastrar_conta()
                print("\n Conta cadastrada com sucesso!".center(100))
            except Exception as e:
                print(f"Erro: {e}")
        elif opcao == "3":
            try:
                Conta.Consultar_saldo()
            except Exception as e:
                print(f"Erro: {e}")
        elif opcao == "4":
            Conta.Realizar_deposito()
        elif opcao == "5":
            Conta.Realizar_saque()
        elif opcao == "6":
            Conta.transferencia()
        elif opcao == "7":
            Dados.listar_clientes()
        elif opcao == "8":
            Dados.listar_contas()
        elif opcao == "9":
            Conta.Emitir_extrato()
        else:
            print("Opção inválida!")

main()