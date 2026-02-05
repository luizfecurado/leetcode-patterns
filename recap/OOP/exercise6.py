class Conta:
    
    def __init__(self,titular,saldo=0):
        self.titular=titular
        self.__saldo=saldo
        
    def depositar(self,valor):
        if valor>0:
            self.saldo+=valor
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
   