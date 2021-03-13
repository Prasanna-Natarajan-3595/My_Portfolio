from flask import Flask
from os import path
from flask_mail import Mail,Message

class app:
    def __init__(self):
        pass       

    def createapp(self):
        from .view import view
        app = Flask(__name__)
        app.config['SECRET_KEY'] = '*$@&*(%@(*YHFRUFHOWUHO*@$(FHSUkgfauguo'
        app.register_blueprint(view, url_prefix='/')
        return app
    