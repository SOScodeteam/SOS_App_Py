from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import pyrebase 

#I really want to migrate this over to firebase for session management
db = SQLAlchemy()





#config = {
#    "apiKey": "INSERT FIREBASE KEYS",
#    "authDomain": "INSERT FIREBASE KEYS",
#    "databaseURL": "INSERT FIREBASE KEYS",
#    "projectId": "INSERT FIREBASE KEYS",
#    "storageBucket": "INSERT FIREBASE KEYS",
#    "messagingSenderId": "INSERT FIREBASE KEYS",
#    "appId": "INSERT FIREBASE KEYS"
#}

#firebase = pyrebase.initialize_app(config)
#auth = firebase.auth()
#db = firebase.database()





def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)
    #auth = pyrebase.initialize_app(config)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import mainroute as main_blueprint
    app.register_blueprint(main_blueprint)

    return app