class Extrato:
    def __init__(self, tipo, valor, data_hora, saldo):
        self.tipo = tipo #define o tipo de transação (depósito, saque, transferência)
        self.valor = valor
        self.data_hora = data_hora
        self.saldo = saldo

    def __str__(self):
        return f"{"-"*50}\nData/Hora: {self.data_hora} \n Tipo: {self.tipo} \n Valor: R${self.valor:.2f} \n Saldo: R${self.saldo:.2f}"

    def __repr__(self):
        return self.__str__()

