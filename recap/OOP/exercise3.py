class Produto():
    
    def __init__(self,nome,estoque,descricao,preco):
        self.nome=nome
        self.estoque=estoque
        self.descricao=descricao
        self.preco=preco
      
    def mostrar_nome(self):
        return self.nome
    
    def mostrar_estoque(self):
        return self.estoque
    
    def mostrar_descricao(self):
        return self.descricao
    
    def mostrar_preco(self):
        return self.preco
    
    def mudar_nome(self,novo_nome):
        self.nome=novo_nome
        
    def mudar_estoque(self,novo_estoque):
        self.estoque=novo_estoque
        
    def mudar_descricao(self,nova_descricao):
        self.descricao=nova_descricao
        
    def mudar_preco(self,novo_preco):
        self.preco=novo_preco
        
    def sumario(self):
        print('Sumário do produto')
        print(f'Produto: {self.nome}')
        print(f'Estoque: {self.estoque}')
        print(f'Descrição: {self.descricao}')
        print(f'Preço: {self.preco}')
 
    
        
produto1=Produto('Produto 1',10,'Produto 1 - Categoria A',20.5)
print(produto1.mostrar_nome())
print(produto1.mostrar_estoque())
print(produto1.mostrar_descricao())
print(produto1.mostrar_preco())
 

produto1.mudar_nome('Produto 2')
produto1.mudar_estoque(20)
produto1.mudar_preco(50.2)
produto1.mudar_descricao('Nova descrição')
 
produto1.sumario()