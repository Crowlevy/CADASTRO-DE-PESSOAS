class Autenticacao:
    def __init__(self,username,senha):
        self.username = username
        self.senha = senha

    def fazerLogin():
        username = str(input("COLOQUE O NOME DE USUÁRIO: "))
        senha = input("COLOQUE A SENHA: ")
        if username == "tecladinho123" and senha == "mano1234":
            return True
        else:
            print("NÃO AUTORIZADO")
            return False
        