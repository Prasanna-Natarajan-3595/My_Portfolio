from flask import Blueprint, render_template, request, flash, jsonify
from .models import contact
from . import db
import json

view = Blueprint('view',__name__)

@view.route('/')
def home():
    if request.method == 'POST':
        name = request.form.get('Name')
        email = request.form.get('Email')
        comments = request.form.get('Comments')
        if len(name)<2:
            flash('Your name must be aleast 2 characters long', category='error')
        elif len(email)<3:
            flash('Enter valid email', category='error')
        elif len(comment)<1:
            flash('Your comment must be aleast 1 characters long', category='error')
        else:
            new_comment = contact(name=name,email=email,comments=comments)
            db.session.add(new_comment)
            db.session.commit()
            flash('Thanks for commenting on my website!!! Get you soon...', category='success')
        
    return render_template('home.html')

@view.route('/test')
def test():
    return render_template('test.html',data=contact)