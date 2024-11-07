import smtplib
from email.mime.text import MIMEText

def send_alert(device):
    # Cria a mensagem de alerta com informações do dispositivo
    msg = MIMEText(f"Dispositivo desconhecido detectado: {device['ip']} ({device['mac']})") # Corpo do e-mail
    msg['Subject'] = 'Alerta de Segurança na Rede' # Assunto do e-mail
    msg['From'] = 'seu_email@gmail.com' # E-mail de origem
    msg['To'] = 'jp.villanova126@gmail.com' # E-mail de destino

    # Conexão com o servidor de e-mail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        # Faz login no servidor de e-mail
        server.login("seu_email@gmail.com", "sua_senha") # E-mail de origem e senha
        # Envia o e-mail de alerta
        server.sendmail(msg['From'], [msg['To']], msg.as_string()) # E-mail de origem, lista de e-mails de destino e mensagem

    # Imprime uma mensagem de confirmação
    print(f"Alerta enviado para {msg['To']}") # E-mail de destino
