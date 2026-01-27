class Conta:
    
    def __init__(self,titular,saldo=0):
        self.titular=titular
        self.__saldo=saldo
        
    def depositar(self,valor):
        self.saldo+=valor
        
    def sacar(self,valor):
        self.saldo-=valor
        
    def saldo(self):
        return self.saldo
    
