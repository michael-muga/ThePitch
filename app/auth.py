from flask import Blueprint, render_template
from . import auth

auth = Blueprint('auth',__name__)

@auth.route('/signup')
def signup():
    return render_template("signup.html")

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")