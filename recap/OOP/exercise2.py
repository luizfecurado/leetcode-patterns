class Pessoa():

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.__senha = senha

    def mostrarnome(self):
        return self.nome

        
    def mostraremail(self):
        return self.email

    def mostrarsenha(self):
        return self.__senha


usuario =   Pessoa("User", "User@user.com", "zxcvb")

print(f"Nome: {usuario.mostrarnome()}")
print(f"Email: {usuario.mostraremail()}")
print(f"senha: {usuario.mostrarsenha()}")