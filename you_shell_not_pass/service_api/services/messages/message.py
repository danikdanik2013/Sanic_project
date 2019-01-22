import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail():
    port = 465
    smtp_server = 'smtp.gmail.com'
    sender_email = 'dpyly1234@gmail.com'
    receiver_gmail = 'danikdanik20133@gmail.com'
    password = input('Type your password: ')
    message = MIMEMultipart('alternative')
    message['Subject'] = 'multiple test'
    message["From"] = sender_email
    message['To'] = receiver_gmail

    text = '''
    Hi,
    How are u?
    '''
    html = '''<html>
      <body>
        <p>Hi,<br>
           How are you?<br>
           <a href="http://www.google.com">Real Google</a> 
           has many great tutorials.
        </p>
      </body>
    </html>'''

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # creating a cerure conneting
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_gmail, message.as_string())

    return True
