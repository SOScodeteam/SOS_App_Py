from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # both derived from usersign up via FireBase
    email = db.Column(db.String(100), unique=True)
    #id = auth.get_account_info(user['idToken'])
    