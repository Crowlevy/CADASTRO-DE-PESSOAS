import re #O RE É UMA BIBLIOTECA DE EXPRESSÕES REGULARES, USAREI PARA VERIFICAR O EMAIL

class Usuarios:
    def __init__(self,cpf,email,idade,nome,data):
        self.cpf = cpf
        self.email = email
        self.idade = idade
        self.nome = nome
        self.data = data

    @classmethod
    def adicionarUsuario(cadastro):
        nome = str(input("QUAL O NOME: "))
        
        idade = input("QUAL A IDADE: ")
        while not idade.isdigit() or int(idade)<=0:
            print("COLOQUE UMA IDADE VÁLIDA")
            idade = input("QUAL A IDADE: ")  

        data = input("DATA DE NASCIMENTO: ")

        cpf = input("COLOQUE O CPF: ")
        while len(cpf) != 11 or not cpf.isdigit():
            print("COLOQUE UM CPF VÁLIDO")
            cpf = input("COLOQUE O CPF: ")
        
        email = input("QUAL O EMAIL: ")
        while not re.match(r"[^@]+@[^@]+\.[^@]+",email):
            print("COLOQUE UM EMAIL VÁLIDO")
            email = input("QUAL O EMAIL: ")
        return cadastro(cpf,email,int(idade),nome,data)
    
    @staticmethod
    def removerUsuario(usuarios):
        nome = str(input("QUAL O NOME DO USUÁRIO QUE DESEJA REMOVER: "))
        for u in usuarios:
            if nome == u.nome:
                usuarios.remove(u)
                print(f"O USUÁRIO {nome} FOI REMOVIDO COM SUCESSO")
            else:
                print("ESSE USUÁRIO NÃO EXISTE")

    @staticmethod
    def buscarPessoa(usuarios):
        pergunta = int(input("DESEJA BUSCAR POR:[1]NOME [2]EMAIL: "))
        if pergunta == 1:
            nome = str(input("COLOQUE O NOME DA PESSOA QUE DESEJA BUSCAR: "))
            for u in usuarios:
                if nome == u.nome:
                    print(f"NOME: {u.nome}, IDADE: {u.idade}, CPF: {u.cpf}, DATA DE NASCIMENTO: {u.data}, EMAIL: {u.email}")
                    return True
            else:
                    print("ESSE NOME NÃO ESTÁ CADASTRADO")
        
        elif pergunta == 2:
            email = input("COLOQUE O EMAIL DO USUÁRIO: ")
            for u in usuarios:
                if email == u.email:
                    print(f"NOME: {u.nome}, IDADE: {u.idade}, CPF: {u.cpf}, DATA DE NASCIMENTO: {u.data}, EMAIL: {u.email}")
                    return True
                else:
                    print("ESSE EMAIL NÃO ESTÁ CADASTRADO")

    @staticmethod
    def organizarUsuarios(usuario,crit):
        if crit == "nome":
            usuario.sort(key=lambda x:x.nome)
        elif crit == "idade":
            usuario.sort(key=lambda x:x.idade)
        elif crit == "data":
            usuario.sort(key=lambda x:x.data)

    @staticmethod
    def editarUsuario(usuarios):
        nomeEditar = str(input("QUAL O NOME DO USUÁRIO QUE DESEJA EDITAR: "))
        for u in usuarios:
            if nomeEditar == u.nome:
                print("USUÁRIO ENCONTRADO")
                u.nome = str(input("COLOQUE O NOME NOVO: "))
                u.idade = input("COLOQUE A IDADE")
                while not u.idade.isdigit() or int(u.idade)<=0:
                    print("IDADE INVÁLIDA")
                    u.idade = input("COLOQUE A NOVA IDADE: ")
                
                u.data = input("COLOQUE A NOVA DATA: ")
                u.cpf = input("COLOQUE O NOVO CPF: ")
                while len(u.cpf) != 11 or not u.cpf.isdigit():
                    print("COLOQUE UM CPF VÁLIDO")
                    u.cpf = input("COLOQUE O NOVO CPF: ")
                
                u.email = input("COLOQUE O NOVO EMAIL: ")
                while not re.match(r"[^@]+@[^@]+\.[^@]+",u.email):
                    print("COLOQUE UM EMAIL VÁLIDO")
                    u.email = input("COLOQUE O NOVO EMAIL: ")
                print("USUÁRIO ALTERADO COM SUCESSO")
                return 
            print("USUÁRIO NÃO ENCONTRADO")
