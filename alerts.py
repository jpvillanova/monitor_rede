import smtplib
from email.mime.text import MIMEText

def send_alert(device): 
    msg = MIMEText(f"Dispositivo desconhecido detectado: {device['ip']} ({device['mac']})")
    msg['Subject'] = 'Alerta de Segurança na Rede'
    msg['From'] = 'seu_email@gmail.com'
    msg['To'] = 'jp.villanova126@gmail.com'

    # Conexão com o servidor de e-mail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server: 
        server.login("seu_email@gmail.com", "sua_senha") 
        server.sendmail(msg['From'], [msg['To']], msg.as_string()) 

    print(f"Alerta enviado para {msg['To']}") 
