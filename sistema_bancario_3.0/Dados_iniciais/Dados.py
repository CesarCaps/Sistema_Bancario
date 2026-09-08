from classes.Cliente import Cliente
from classes.Conta import Conta

# 1. Criando instâncias reais de Clientes
Clientes = [
    Cliente(nome="Carlos Silva", cpf="123.456.789-00", data_nascimento="14/05/1988", endereco="Rua das Flores, 123 - São Paulo/SP"),
    Cliente(nome="Mariana Souza", cpf="987.654.321-11", data_nascimento="22/11/1993", endereco="Av. Central, 1540 - Apt 42 - Rio de Janeiro/RJ"),
    Cliente(nome="Roberto Alencar", cpf="456.123.789-22", data_nascimento="03/01/1975", endereco="Alameda dos Anjos, 89 - Belo Horizonte/MG"),
    Cliente(nome="Juliana Costa", cpf="789.456.123-33", data_nascimento="30/08/2001", endereco="Rua Sergipe, 405 - Curitiba/PR")
]

# 2. Criando instâncias reais de Contas Correntes
Contas_corrente = [
    Conta(tipo="Corrente", cpf="123.456.789-00", numero_conta="1001-5", saldo=2500.50),
    Conta(tipo="Corrente", cpf="987.654.321-11", numero_conta="2002-3", saldo=150.00),
    Conta(tipo="Corrente", cpf="456.123.789-22", numero_conta="3003-1", saldo=12750.80),
    Conta(tipo="Corrente", cpf="789.456.123-33", numero_conta="4004-9", saldo=0.00)
]

# 3. Criando instâncias reais de Contas Poupanças
Contas_poupanca = [
    Conta(tipo="Poupança", cpf="123.456.789-00", numero_conta="1001-5", saldo=0.00),
    Conta(tipo="Poupança", cpf="987.654.321-11", numero_conta="2002-3", saldo=0.00),
    Conta(tipo="Poupança", cpf="456.123.789-22", numero_conta="3003-1", saldo=0.00),
    Conta(tipo="Poupança", cpf="789.456.123-33", numero_conta="4004-9", saldo=0.00)
]


def listar_clientes():
    print(f"|{"Nome":^50}| {"CPF":^15}| {"Data de Nascimento":^20}| {"Endereco":^50}|")
    print("-"*141)
    for cliente in Clientes:
        print(f"|{cliente.nome:^50}| {cliente.cpf:^15}| {cliente.data_nascimento:^20}| {cliente.endereco:^50}|")
        print("-"*141)

def listar_contas():
    while True:
        tipo_conta = int(input("1-Contas Corrente / 2-Contas Poupança: "))
        
        if tipo_conta == 1:
            lista_alvo = Contas_corrente
        elif tipo_conta == 2:
            lista_alvo = Contas_poupanca
        else:
            print("Tipo de conta inválido! Tente novamente.")
            continue

        # Cabeçalho da tabela com aspas corrigidas
        print(f"|{'Nome':^50}|{'CPF':^15}|{'Conta':^8}|{'Saldo':^12}|")
        print("-" * 91)

        # Iteração baseada estritamente em Objetos
        for conta in lista_alvo:
            titular = encontrar_cliente(conta.cpf)
            if titular == None:
                break
            else:
                saldo_formatado = f"R$ {conta.saldo:.2f}"
                # Impressão acessando atributos de objetos externos
                print(f"|{titular:^50}|{conta.cpf:^15}|{conta.numero_conta:^8}|{saldo_formatado:^12}|")
                print("-" * 91)

        break

def encontrar_cliente(cpf):
    CPF = cpf
    for cliente in Clientes:
        if cliente.cpf == CPF:
            titular = cliente.nome
            break
        else:
            titular =  None
    return titular