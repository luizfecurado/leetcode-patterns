class Pessoa():

    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def mostrardados(self):
        print(f"Nome completo: {self.nome} {self.sobrenome}")
        print(f"Idade: {self.idade}")



pessoa = Pessoa("Luiz","Felipe", 21)
print(pessoa.nome)
print(pessoa.sobrenome)
print(pessoa.idade)
pessoa.mostrardados()