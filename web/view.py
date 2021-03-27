from flask import Blueprint, render_template, request, flash,redirect,url_for,session
from flask_mail import Mail,Message
from .__init__ import *

view = Blueprint('view',__name__)

@view.route('/', methods=['GET', 'POST'])
def home():
   if request.method == 'POST':
        name = request.form.get('Name')
        email = request.form.get('Email')
        comments = request.form.get('Comments')
        if len(name)<2:
           flash('Your name must be aleast 2 characters long', category='error')
        elif len(email)<3:
           flash('Enter valid email', category='error')
        elif len(comments)<1:
           flash('Your comment must be aleast 1 characters long', category='error')
        else:
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
              
           sendmessage('Prasannan-thanks for commenting','noreplyprasanna@gmail.com',[email],f"""Dear {name},
I have received your comment.Thanks for commenting on my website.
I will get you soon.Have a nice day!
Don't reply to this email!!!
             Thanks!!!
Regards
Prasanna-bot""")
           sendmessage('Prasannan-You got a new comment on your website','noreplyprasanna@gmail.com',['prasannanatarajan3595@gmail.com'],f"""Dear Prasanna,
You got a new comment on your website...
Name:{name}
Email:{email}
Comment:{comments}

             Thanks!!!
Regards
Prasanna-bot""")
           flash('Thanks for commenting on my website!!! Get you soon...', category='success')
        
    
   return render_template('home.html')