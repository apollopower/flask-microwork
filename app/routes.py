from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jonas'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Snorlax'},
            'body': 'Zzzzzzzzzzzz...'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
            