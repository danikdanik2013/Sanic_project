import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(email, html):
    port = 465
    smtp_server = 'smtp.gmail.com'
    sender_email = 'dpyly1234@gmail.com'
    password = ''
    message = MIMEMultipart('alternative')
    message['Subject'] = 'multiple test'
    message["From"] = sender_email
    message['To'] = email

    text = '''
    Hi,
    How are u?
    '''
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # creating a cerure conneting
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, email, message.as_string())

    return email
