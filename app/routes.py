from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jacob'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Scotland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so shit!'
        },
        {
            'author': {'username': 'Random Dude'},
            'body': 'I like trains!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login page', form=form)
