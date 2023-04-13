import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = 'donfortunet.df@gmail.com'
    password = 'kktoyewnkmctutke'
    receiver_email = 'osowoayiobi@gmail.com'


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as file:
        file.login(username, password)
        file.sendmail(username, receiver_email, message)



