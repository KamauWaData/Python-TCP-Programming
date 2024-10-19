import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

myServer = smtplib.SMTP('smtp.world4you.com', 25)

myServer.ehlo()

with open('pass.txt', 'r') as f:
    password = f.read().strip()

myServer.login('mailtesting@kahash.com', password)

msg = MIMEMultipart()
msg['From'] = 'Neuraline'
msg['To'] = 'testing'
msg['Subject'] = 'Just testing yow!'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'learn.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
myServer.sendmail('mailtesting@neuraline', 'testmail@spamail.de', text)