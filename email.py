from flask import Flask
from flask_mail import Mail, Message
app = Flask(__name__)

app.config.update(dict(
    MAIL_SERVER = 'smtp.googlemail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'drnascarsocial',
    MAIL_PASSWORD = '@Dr.Bool16'
))

mail = Mail(app)

@app.route('/process_email', methods=['POST'])
def process_email():
    msg = Message('Test', sender='drnascarsocial@gmail.com', recipients=['ajguarni@buffalo.edu'])
    msg.body = 'This is a test email' #Customize based on user input
    mail.send(msg)

    return 'done'