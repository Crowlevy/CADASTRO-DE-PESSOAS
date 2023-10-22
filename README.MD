# SISTEMA DE CADASTRO DE USUÁRIOS, COM EXPORTAÇÃO PARA EXCEL E EMAIL


### Esse é um projeto em pyton para cadastrar usuários novos e salvá-los em uma planilha em excel ou enviar e-mails para todos os que estão cadastrados

## FEATURES
### Exportar Para Excel
```python
from exportExcel import exportarExcel
workbook = Workbook()
    sheet = workbook.active
    sheet.append(["NOME","IDADE","CPF","DATA DE NASCIMENTO","EMAIL"])
        
    for usuario in usuarios:
        sheet.append([usuario.nome,usuario.idade,usuario.cpf,usuario.data,usuario.email])
    workbook.save(filename="usuarios_cadastrados.xlsx")
    '''Ele cria uma linha para cada usuário'''
```
### Enviar E-mails para usuários logados
```python
def enviarMensagem(email):
        remetente = "emailenviar@gmail.com"
        senha = "senha123"
        destinatario = email
        assunto = "MACACO"
        corpoEmail = """
        <p>AAAAAAAAAAAAAAAAAA</p>
        <p>mano</p>"""

        sender = EnviarEmail(remetente, senha)
        sender.enviar_email(destinatario, assunto, corpoEmail)
        print("E-MAIL ENVIADO!!")
```

## BIBLIOTECAS NECESSÁRIAS
* re
* openpyxl
* smtplib
* email

```bash
$pip install re openpyxl smtplib email 
```

## OBRIGADO
#### CASO TENHA ALGUM BUG, POR FAVOR REPORTAR OU ACRESCENTAR UM FORK PARA AJUDAR:)
<img src="voceRS.jpeg" width="40%" margin="auto"><br>