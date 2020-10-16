import json
from flask import Flask, render_template,url_for, request
from forms import SignupForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'aa0eb2fcfae25481525f3fe11871c26a'
@app.route('/')
def main():
    return render_template('index.html') 

@app.route('/signup')
def signup():
    form = SignupForm()
    return render_template('signup.html', title = 'Sign Up', form = form) 
    
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title = 'Log In', form = form) 

if __name__ == '__main__':
    app.run()
