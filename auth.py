from flask import *
import pyrebase #included for authentication
from flask_login import login_user, logout_user, login_required

config = {
    "apiKey": "INSERT FIREBASE KEYS",
    "authDomain": "INSERT FIREBASE KEYS",
    "databaseURL": "INSERT FIREBASE KEYS",
    "projectId": "INSERT FIREBASE KEYS",
    "storageBucket": "INSERT FIREBASE KEYS",
    "messagingSenderId": "INSERT FIREBASE KEYS",
    "appId": "INSERT FIREBASE KEYS"
} #these are the API keys for firebase

#this initializes access
firebase = pyrebase.initialize_app(config)
approved = firebase.auth()

auth = Blueprint('auth', __name__)

@auth.route('/signup/')
def signup():
    return render_template('signup.html')


#planned to move to main thread
@auth.route('/submit_feedback/')
def submit_feedback():
    return render_template('submit_feedback.html')

@auth.route('/view_feedback/')
def view_feedback():
    return render_template('view_feedback.html')

@auth.route('/signup/', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    password = request.form.get('password')
    #firebase createuser
    user = approved.create_user_with_email_and_password(email, password)
    return redirect(url_for('auth.login'))
    #return render_template('signup.html')

@auth.route('/login/')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    try:
        user = approved.sign_in_with_email_and_password(email, password)
        login_user(user, remember=remember)  
        return redirect(url_for('mainroute.profile'))
    except:
        return redirect(url_for('auth.login')) #this is the poor mans way to catch the authentication errors

        
#@auth.route('/logout/')
#def logout():
#    return 'Logout'

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('mainroute.index'))