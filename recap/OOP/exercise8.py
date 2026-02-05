class Pessoa:
  def __init__(self,nome,idade,telefone):
    self.nome=nome
    self.idade=idade
    self.__telefone=telefone
 
  def resumo(self):
    print(f'Nome: {self.nome}')
    print(f'Idade: {self.idade}')
    print(f'Telefone: {self.__telefone}')
 
 
class PessoaUniversidade(Pessoa):
  def __init__(self,nome,idade,telefone,universidade):
    super().__init__(nome,idade,telefone)
    self.universidade=universidade
 
  def resumo(self):
    super().resumo()
    print(f'Universidade: {self.universidade}')