from datetime import datetime
from interface.Interface import Cabecalho_cadastro_cliente
import re #verificador de formato de CPF

class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

    def __str__(self):
        return f"Cliente: {self.nome}\n CPF: {self.cpf}\n Data de nascimento: {self.data_nascimento}\n Endereço: {self.endereco}"
    
    def __repr__(self):
        return self.__str__()


    
def Cadastrar_cliente():
    import Dados_iniciais.Dados as Dados
    Cabecalho_cadastro_cliente()
    print("Cadastro de Cliente")
    nome = input("Digite o nome do cliente: ")
    while True:
        cpf = input("Digite o CPF do cliente: ")
        if verificar_cpf(cpf):
            break
        else:
            print("CPF inválido! Tente novamente.")

    while True: # O loop continua até o usuário acertar o formato
        try:
            data_input = input("Digite a data de nascimento do cliente (dd/mm/aaaa): ")
            # Se a conversão funcionar, quebra o loop e segue o código
            data_nascimento = datetime.strptime(data_input, "%d/%m/%Y")
            break 
        except ValueError:
            print("Data de nascimento inválida! Tente novamente.")
    endereco = input("Digite o endereço do cliente: ")
    
    cliente = Cliente(nome, cpf, data_nascimento, endereco)
    Dados.Clientes.append(cliente)
    return cliente

def verificar_cpf(cpf) -> bool:
    padrao = r"^(\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})$" 
    return bool(re.match(padrao, cpf))  # Retorna True se o CPF estiver no formato correto, caso contrário, retorna False

