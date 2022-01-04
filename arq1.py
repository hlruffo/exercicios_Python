import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# importa login e senha de outro arquivo
from secret import login
from secret import senha

# configura remetente e destino
fromaddr = "suporte@ligosim.com"
toaddr = "hlruffo@gmail.com"

# configura mensgam
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Teste de envio de emails"
body = " Hello World!\nEste email foi enviado por um robô que em breve funcionará de forma autonoma para a LigoSIM"
msg.attach(MIMEText(body, 'plain'))

# anexo
filename = "Comunicado.pdf"
anexo = open('Comunicado.pdf', 'rb')
p = MIMEBase('application', 'octet-stream')
p.set_payload(anexo.read())
encoders.encode_base64(p)

p.add_header('Content-Disposition', 'attachment; filename=%s' % filename)
msg.attach(p)

# conecta ao servidor de email e envia
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(login, senha)
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()
