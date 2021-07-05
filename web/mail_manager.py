from flask import Flask
from flask_mail import Mail,Message

def sendmessage(msghead,sender,recipients,body):
              app = Flask(__name__)
              mail = Mail(app)
              app.config['MAIL_SERVER']='smtp.gmail.com'
              app.config['MAIL_PORT'] = 465
              app.config['MAIL_USERNAME'] = 'noreplyprasanna@gmail.com'
              app.config['MAIL_PASSWORD'] = 'Prasanna@1234'
              app.config['MAIL_USE_TLS'] = False
              app.config['MAIL_USE_SSL'] = True
              mail = Mail(app)
              msg = Message(msghead,sender = sender,recipients = recipients)
              msg.body = body
              mail.send(msg)