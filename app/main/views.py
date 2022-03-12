from flask import render_template,request,redirect,url_for
from . import main
from . forms import LoginForm, RegisterForm, PitchForm, CommentForm


@main.route('/')
def index():

    return render_template('index.html')


@main.route('/error')
def error():

    return render_template('error.html')