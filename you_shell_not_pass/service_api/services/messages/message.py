import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from itsdangerous import URLSafeTimedSerializer
from jinja2 import Environment, PackageLoader
from sanic.response import text

from service_api.app import app

env = Environment(loader=PackageLoader('my_blueprint', 'templates'))
template = env.get_template('activation.html')


def send_confirmation_email(email):
    confirm_serializer = URLSafeTimedSerializer('Thisissercet!')

    confirm_url = app.url_for(
        'post_handler',
        token=confirm_serializer.dumps('danikdanik20133@gmail.com', salt='email-confirmation-salt'),
        _external=True)
    content = template.render(confirm_url=confirm_url)

    send_mail(email, content)


@app.route('confirm_token/<token>')
async def post_handler(request, token):
    return text('token - {}'.format(token))


def send_mail(email, content):
    port = 465
    smtp_server = 'smtp.gmail.com'
    sender_email = 'dpyly1234@gmail.com'
    password = ''
    message = MIMEMultipart('alternative')
    message['Subject'] = 'multiple test'
    message["From"] = sender_email
    message['To'] = receiver_gmail

    text = '''
    Hi,
    How are u?
    '''

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(content, 'html')

    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # creating a cerure conneting
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_gmail, message.as_string())

    return True


