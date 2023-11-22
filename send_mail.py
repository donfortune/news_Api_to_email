import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = 'donfortunet.df@gmail.com'
    password = 'xxxxxxxxxxxxxxx'
    receiver_email = 'XXXXXXXXXX'


    context = ssl.create_default_context()  #security context 
    with smtplib.SMTP_SSL(host, port, context=context) as file:
        file.login(username, password)
        file.sendmail(username, receiver_email, message)



