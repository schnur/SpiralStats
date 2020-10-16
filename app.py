import json
from flask import Flask, render_template,url_for, request, redirect
from forms import SignupForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'aa0eb2fcfae25481525f3fe11871c26a'
@app.route('/')
def main():
    return render_template('index.html') 


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    if request.method == "GET":
        form = SignupForm()
        return render_template('signup.html', title = 'Sign Up', form = form) 
    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        print("Username :", username)
        print("Passwprd :", password)
        print("Confirm Password :", confirm_password)
        return redirect(url_for('home'))
    
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == "GET":
        form = LoginForm()
        return render_template('login.html',title = 'Log In', form = form) 
    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        print("Username :", username)
        print("Passwprd :", password)
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()
