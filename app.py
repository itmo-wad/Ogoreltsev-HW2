from flask import Flask
from flask import render_template, redirect, session
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = b'\x1e\xc6\x0f\x94_\xbe\x0c\x1f\x05*\xeeaS\xd9"\xa0'

client = pymongo.MongoClient('localhost', 27017, username='admin', password='admin')
db = client.user_login_system

def login_requiered(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap

from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
@login_requiered
def profile():
    return render_template('profile.html')

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')

