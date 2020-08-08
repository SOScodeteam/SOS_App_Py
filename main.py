from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

mainroute = Blueprint('mainroute', __name__)

@mainroute.route('/')
def index():
    return render_template('index.html')

#@mainroute.route('/submit_feedback/')
#def submit_feedback():
#    return render_template('submit_feedback.html')

#@mainroute.route('/view_feedback/')
#def view_feedback():
#    return render_template('view_feedback.html')

@mainroute.route('/profile/')
#@login_required
def profile(name="default"):
    #return render_template('profile.html', name=current_user.name)
    return render_template('profile.html')