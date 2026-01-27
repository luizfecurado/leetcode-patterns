from datetime import datetime
class Conta:

    
    def __init__(self,titular,saldo=0):
        self.titular=titular
        self.__saldo=saldo
        self.__extrato=[]
        
    def depositar(self,valor):
        if valor>0:
            self.saldo+=valor
            data=datetime.today().strftime('%d/%m/%Y')
            self.__extrato.append(['Depósito',valor,data])
            return 'Depósito realizodo com sucesso.'
        return 'Valor inválido.'
        
    def sacar(self,valor):
        if valor>0:
            if valor<=self.__saldo:
                self.__saldo-=valor
                return 'Saque realizado com sucesso.'
            return 'Saldo insuficiente.'
        return 'Valor inválido'
        
    def saldo(self):
        return self.saldo
    
    def resumo(self):
        print(f'Titular: {self.__nome}')
        print(f'Saldo: R$ {self.__saldo}')
        
    def extrato(self):
        for operacao in self.__extrato:
            print(f'Data: {operacao[2]}')
            print(f'Operação: {operacao[0]}')
            print(f'Valor: R$ {operacao[2]:.2f}')
            print()