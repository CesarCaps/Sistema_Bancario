#parâmetros iniciais
saldo = valor_sacado = numero_saques = 0
limite_diario = 500
LIMITE_SAQUES = 3
extrato = []
usuarios = [{"CPF" : 1234, "nome" : "cesar", "data_nascimento" : "06/11/1998", "Endereço" : "rua tal"}] #dados iniciados para facilitar testes
contas = [{"conta" : 1, "CPF" : 1234, "agencia" : "0001", "saldo" : 1500, "extrato" : [], "quantidade_saque" : 0, "valor_saque" : 0}] #dados iniciados para facilitar testes

def cadastro_usuario():
    cpf = input("informe seu CPF: ")
    consulta = filtrar_usuario(cpf, usuarios)
    if consulta:
        nome = input("informe seu nome: ")
        data_nascimento = input("informe sua data de nacimento (dd/mm/aaaa): ")
        endereco = input("informe seu endereço: ")
        usuarios.append({
            "CPF" : cpf, 
            "nome" : nome, 
            "data_nascimento" : data_nascimento, 
            "Endereço" : endereco
            })
        print(f"{'Cadastro criado com sucesso!':_^100}")
    else:
        print("Erro: Este CPF já consta no sistema.")
    
def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            print(f"CPF {cpf} já está cadastrado")
            return False
    return True

def criar_conta():
    cpf_usuario = input("informe o CPF que será titular da conta: ")
    confirmacao = checar_usuario(cpf_usuario, usuarios)
    if confirmacao == True:
        agencia = '0001'
        numero_conta = (contas[-1] + 1)
        contas.append({
            'conta' : numero_conta,
            'CPF' : cpf_usuario, 
            'agencia' : agencia, 
            'saldo' : 0,
            'extrato' : [],
            'quantidade_saque' : 0, 
            'valor_saque' : 0
            })
        print(f"Conta {numero_conta} criada com sucesso para o CPF {cpf_usuario}!")
    else:
        print("Erro: Usuário não encontrado. É necessário cadastrar o usuário antes de criar uma conta.")

def checar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            return True
    return False

def buscar_conta(conta_a_buscar, contas):  # verifica se a conta existe
    for conta in contas:
        if conta["conta"] == conta_a_buscar:
            return True
    return False

def conta_encontrada(busca, contas): #a conta buscada já está com a existência verificada
    contas_filtradas = [conta for conta in contas if conta["conta"] == busca]
    return contas_filtradas[0] if contas_filtradas else None

def trazer_criente(cpf, usuarios): #trás o nome do cliente dono da conta
    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            nome_titular = usuario["nome"]
            break
    return nome_titular
            
def deposito():
    conta_a_buscar = int(input("informe a conta a receber o depósito: "))
    confirmacao = buscar_conta(conta_a_buscar, contas) #função de verificação de existência de conta
    if confirmacao:
        conta_deposito = conta_encontrada(conta_a_buscar, contas) #tras a conta já verificada
        cliente = trazer_criente(conta_deposito["CPF"], usuarios)
        print(f"{'conta encontrada':_^100}")
        print(f"conta associada ao cliente {cliente}")
        valor = float(input("informe o valor a ser depositado: R$"))
        if (valor < 0):
            print("Não é possível inserir valores negativos!")
        else: 
            conta_deposito['saldo'] += valor
            conta_deposito['extrato'].append(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso na Conta: {conta_deposito['conta']}")
            print(f"Novo saldo: R${conta_deposito['saldo']:.2f}")
    else:
        print("Conta inexistente, tente novamente!")

def saque():
    conta_a_buscar = int(input("informe a conta a realizar o saque: "))
    confirmacao = buscar_conta(conta_a_buscar, contas)
    if confirmacao:
        conta_saque = conta_encontrada(conta_a_buscar, contas)
        if conta_saque["quantidade_saque"] >= LIMITE_SAQUES:
            print("Limite de saques diários atingido.")
        else:
            cliente = trazer_criente(conta_saque["CPF"], usuarios)
            print(f"conta associada ao cliente {cliente}")
            valor = float(input("Digite o valor de Saque: R$"))
            if (conta_saque["valor_saque"] + valor) >= limite_diario:
                print("Valor limite de R$500,00 diário excedido!")
            else:
                if (valor > conta_saque["saldo"]):
                    print("Saldo insuficiente!")
                else:
                    conta_saque["saldo"] -= valor
                    conta_saque["valor_saque"] += valor
                    conta_saque["quantidade_saque"] += 1
                    conta_saque['extrato'].append(f"Saque: R${valor:.2f}")
                    print(f"Saque de R${valor:.2f} realizado com sucesso na Conta: {conta_saque['conta']}")
                    print(f"Novo saldo: R${conta_saque['saldo']:.2f}")
    else:
        print("Conta inexistente!")

def extrato():
    conta_a_buscar = int(input("informe a conta a receber o extrato: "))
    confirmacao = buscar_conta(conta_a_buscar, contas) #função de verificação de existência de conta
    if confirmacao:
        conta_extrato = conta_encontrada(conta_a_buscar, contas) #trás a conta já verificada
        print(f"{'conta encontrada':_^100}")
        print(f"conta associada ao CPF {conta_extrato["CPF"]}") #alterar para trazer o nome do cliente
        print("exibindo histórico de entradas de saldo: ")
        print(conta_extrato["extrato"])
        print(f"Saldo total: R${conta_extrato["saldo"]:.2f}")
    else:
        print("Conta inexistente, tente novamente!")

def menu_principal():
    menu = ['Encerrar', 'Cadastro de Usuários', 'Criar Contas', 'Depósito', 'Saque', 'Extrato']
    print(f"{'Menu Principal':_^100}")
    for c in range(0, len(menu)):
        print(f"{c} - {menu[c]}")    

def main():
    while True:
        cabecalho() #chama a função cabeçalho
        menu_principal() # chama a função menu principal
        opcao = int(input("Selecione a Alternativa de sua escolha: "))
    
        if (opcao == 1):
            cadastro_usuario()
        elif (opcao == 2):
            criar_conta()
        elif(opcao == 3):
            deposito()
        elif(opcao == 4):
            saque()
        elif(opcao == 5):
            extrato()
        elif(opcao == 0):
            break
        else:
            print("Opção inválida!")

def cabecalho():
    print("=" * 100)
    print(f"{'SISTEMA BANCÁRIO':^100}")
    print("=" * 100)
    





main()