#CADASTRO DE PESSOAS
from exportExcel import exportarExcel
from usuarios import Usuarios
from autenticacao import Autenticacao
from enviarEmail import EnviarEmail

def main():
    '''
    autenticado = False
    while not autenticado:
        autenticado = Autenticacao.fazerLogin()'''#AUTENTICAÇÃO POR SENHA, CASO QUEIRA REMOVER É SIMPLES
                                                
    usuariosComputados = []
    while True:
        try:
            print("BEM VINDO AO PROGRAMA DE CADASTRO\n")
            print("[1]ADICIONAR USUÁRIO")
            print("[2]VERIFICAR USUÁRIOS")
            print("[3]BUSCAR PESSOAS")
            print("[4]REMOVER USUÁRIO")
            print("[5]ORGANIZAR USUÁRIOS")
            print("[6]EXPORTAR PARA EXCEL")
            print("[7]ORGANIZAR USUÁRIOS")
            print("[8]ENVIAR E-MAILS")
            print("[0]SAIR")

            pergunta = int(input("COLOQUE O QUE DESEJA FAZER: "))

            if pergunta == 1:
                usuarioNovo = Usuarios.adicionarUsuario()
                usuariosComputados.append(usuarioNovo)
            elif pergunta == 2:
                for usuario in usuariosComputados:
                    print(f"NOME:{usuario.nome},\n IDADE:{usuario.idade},\n CPF:{usuario.cpf},\n DATA DE NASCIMENTO:{usuario.data},\n EMAIL:{usuario.email}\n\n")
                if usuariosComputados == []:
                    print("ESTÁ VAZIO")
            elif pergunta == 3:
                Usuarios.buscarPessoa(usuariosComputados)
            elif pergunta == 4:
                Usuarios.removerUsuario(usuariosComputados)
            elif pergunta == 5:
                Usuarios.organizarUsuarios(usuariosComputados)
            elif pergunta == 6:
                exportarExcel(usuariosComputados)
            elif pergunta==7:
                Usuarios.editarUsuario(usuariosComputados)
            elif pergunta ==8:
                for usuario in usuariosComputados:
                    EnviarEmail.enviarMensagem(usuario.email)
            elif pergunta == 0:
                print("OBRIGADO, VOLTE SEMPRE")
                break

        except ValueError as ve:
            print(f"OCORRE UM ERRO DE {ve}, POR FAVOR TENTE NOVAMENTE")
if __name__ == "__main__":
    main()
