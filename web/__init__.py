from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "contacts.db"

def create_app():
    from .view import view
    from .models import contact


    app = Flask(__name__)
    app.config['SECRET_KEY'] = '*$@&*(%@(*YHFRUFHOWUHO*@$(FHSUkgfauguo'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    app.register_blueprint(view, url_prefix='/')
    create_database(app)

    return app

    
def create_database(app):
    if not path.exists('web/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
