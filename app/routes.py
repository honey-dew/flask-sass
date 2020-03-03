from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Gugun'}
    posts = [
        {
            'author':{'username':'Gugun'},
            'body':'Hello from Flask'
        },
        {
            'author':{'username':'Adi'},
            'body':'Hello from SASS'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)