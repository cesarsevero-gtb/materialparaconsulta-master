#import dos pacotes necessários
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


#criação de um objeto de mensagem
msg = MIMEMultipart()
texto = "Estou enviando um e-mail com python"

#parâmetros
senha = "Rasec123456@"
msg['From'] = 'direito1boab@gmail.com'
msg['To'] = 'amiguinho.c@gmail.com'
msg['Subject'] = "python"

#criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

#criação do servidor

server = smtplib.SMTP('smtp.gamil.com: 587')
server.starttls()

#Login na conta para envio
server.login(msg['From'], senha)

#envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

#encerramento do servidor
server.quit()


print('Mensagem enviada com sucesso')