from flask import Flask, render_template, url_for, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password1234'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////var/www/WebPage/Database/dat1.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column('User_id', db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    username = db.Column(db.String(30), unique=False)
    password = db.Column(db.String(40), unique=False)
#    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

@app.route("/loginOrsignup", methods=['POST', 'GET'])
def loginOrsignup():
    return render_template('LoginOrSignup.html')

@app.route("/Login", methods=['POST', 'GET'])
def Login():
    if request.method == 'POST':
        if not request.form.get('email') or not request.form.get('password'):
            flash('Please enter all the fields', 'error')
        else:
            email1 = request.form.get('email')
            password1 = request.form.get('password')
            Login.missing_email = db.session.query(User.email).filter_by(email=email1).scalar()
            if email1 == Login.missing_email:
                hashed_pass_retrieve = db.session.query(User.password).filter_by(email=email1).scalar()
                if bcrypt.checkpw(password1.encode('utf-8'), hashed_pass_retrieve):
                    return redirect(url_for('LoginEnd'))
                else:
                    return "Email or Password does not match, Please try again!"
            else:
                return "Email or Password does not match, Please try again!" 
    return render_template('Login.html')

@app.route("/SignUp", methods=['POST', 'GET'])
def SignUp():
    if request.method == 'POST':
        if not request.form.get('email') or not request.form.get('username') or not request.form.get('password'):
            flash('Please enter all the fields', 'error')
        else:
            user_email = request.form.get('email')
            user_username = request.form.get('username')
            user_password = request.form.get('password')
            exist_email = db.session.query(User.email).filter_by(email=user_email).scalar()
            if user_email == exist_email:
                return 'Email Already in use, Please try another email!'
            else:
                hashed_pass = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt(rounds=12))
                new_user = User(user_email, user_username, hashed_pass)
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('Login'))
    return render_template('SignUp.html')

@app.route("/LoginEnd", methods=['POST', 'GET'])
def LoginEnd():
    Login()
    display_user = db.session.query(User.username).filter_by(email=Login.missing_email).scalar()
    return render_template("LoginEnd.html", display_user=display_user)

if __name__ == "__main__":
    app.run()

