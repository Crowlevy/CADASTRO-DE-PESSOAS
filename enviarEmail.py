#ESSA É UMA ESTRUTURA BEM BÁSICA PARA ENVIAR EMAILS, PODE SER ADICIONADO UM TEMPORIZADOR DIÁRIO DE EMAILS,CASO QUEIRA

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''EM UMA NOVA ATUALIZAÇÃO DO GOOGLE A PARTE DE SENHA MUDOU COMPLETAMENTE, AGORA NÃO É MAIS POSSÍVEL PERMITIR
   O ACESSO DE APPS MENOS SEGUROS, PARA CONSEGUIR ENVIAR COMO ANTES É NECESSÁRIO QUE HABILITE A VERIFICAÇÃO DE 
   DUAS ETAPAS, DENTRO DELA IRÁ APARECER UMA PARTE CHAMADA "Senha de apps" NESSA PARTE VOCÊ VAI GERAR UMA NOVA.
   QUANDO GERADA A SENHA NOVA, VOCÊ COPIA E COLA SOMENTE NA PARTE DA SENHA, TORNANDO POSSÍVEL ENVIAR'''

class EnviarEmail:
    def __init__(self, remetente, senha):
        self.remetente = remetente
        self.senha = senha
        self.servidor_smtp = 'smtp.gmail.com'
        self.porta_smtp = 587

    def enviar_email(self, destinatario, assunto, corpo):
        msg = MIMEMultipart()
        msg['From'] = self.remetente
        msg['To'] = destinatario
        msg['Subject'] = assunto

        msg.attach(MIMEText(corpo, 'html'))

        server = smtplib.SMTP(self.servidor_smtp, self.porta_smtp)
        server.starttls()
        server.login(self.remetente, self.senha)
        server.sendmail(self.remetente, destinatario, msg.as_string())
        server.quit()

    def enviarMensagem(email):
        remetente = "emailenviar@gmail.com"
        senha = "senha123"#ONDE É NECESSÁRIO A CRIAÇÃO DE UM PROJETO E SENHA NO GOOGLE
        destinatario = email
        assunto = "MACACO"
        corpoEmail = """
        <p>AAAAAAAAAAAAAAAAAA</p>
        <p>mano</p>"""#A ESTRUTURA DO CORPO É IDÊNTICA A DO HTML

        sender = EnviarEmail(remetente, senha)
        sender.enviar_email(destinatario, assunto, corpoEmail)
        print("E-MAIL ENVIADO!!")

