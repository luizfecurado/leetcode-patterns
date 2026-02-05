class Lampada:
    
    def __init__(self,cor,voltagem,luminosidade):
        self.__cor=cor
        self.__voltagem=voltagem
        self.__luminosidade=luminosidade
        self.__ligada=False
    
    def verificar_ligada(self):
        return self.__ligada
 
    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada=False
            return self.__ligada
        else:
            self.__ligada=True
            return self.__ligada
            
lamp1=Lampada('amarela',110,80)
print(lamp1.verificar_ligada())  
print(lamp1.ligar_desligar())  
print(lamp1.ligar_desligar())  