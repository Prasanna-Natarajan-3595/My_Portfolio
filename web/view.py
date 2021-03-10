from flask import Blueprint, render_template, request, flash,redirect,url_for,session
from .models import contact
from . import db
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
           new_comment = contact(name=name,email=email,comments=comments)
           db.session.add(new_comment)
           db.session.commit()
           flash('Thanks for commenting on my website!!! Get you soon...', category='success')
        
    
    return render_template('home.html')

@view.route('/test')
def test():
    return render_template('test.html')

@view.route('/login', methods=['POST','GET'])
def login():
   if request.method == 'POST':
      email = request.form.get('email')
      password = request.form.get('password')
      if email == 'prasannanatarajan3595@gmail.com':
         if password == '2005':
            flash('Login successfull!', category='sucess')
            session['email'] = email
            session['password'] = password
            return redirect(url_for('view.admin'))
         else:
            flash('Incorrect password!',category='error')
      else:
         flash('Incorrect email!',category='error')
   return render_template('login.html')

@view.route('/admin')
def admin():
   if session['email'] == 'prasannanatarajan3595@gmail.com':
      if session['password'] == '2005':
         contacts = contact.query.all()
         return render_template('admin.html',comment=contacts)
   else:
      return redirect(url_for('view.login'))

@view.route('/signout')
def signout():
   session.pop('email', None)
   session.pop('password', None)
   flash('You are logged out!', category='success')
   return redirect(url_for('view.home'))