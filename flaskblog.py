from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
# Secret key
app.config['SECRET_KEY'] = 'e33cc6fcf38be4c8f4062ab1fae038b3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# create an SQLAlchemy Database instance
db = SQLAlchemy(app)

from models import User, Post



posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 26, 2020'
    },
    {
        'author': 'James Gonzales',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 14, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form) 

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check username and password!', 'danger')    
    return render_template('login.html', title='Login', form=form)        

if __name__ == '__main__':
    app.run(debug=True)