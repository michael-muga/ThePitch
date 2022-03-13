from crypt import methods
from flask import render_template,request,redirect,url_for
from . import main
from . forms import LoginForm, RegisterForm, PitchForm, CommentForm, UpdateProfile
from ..models import User, Pitch, Comment
from flask_login import login_required, current_user, logout_user
from .. import db, photos


@main.route('/')
def index():

    return render_template('index.html')


@main.route('/error')
def error():

    return render_template('error.html')

@main.route('/pitch', methods = ['GET','POST'])
@login_required
def pitch():
    form = PitchForm()

    if form.validate_on_submit():
        pitch = Pitch(owner_id=current_user.id, title=form.title.data,
                      category=form.category.data, description=form.description.data)
        form.title.data = ''
        form.category.data = ''
        form.description.data = ''

        db.session.add(pitch)
        db.session.commit()
    return render_template('pitch.html', form=form)

@main.route('/user/<uname>')
@login_required
def profile(uname):

    pitch = Pitch.query.filter_by(id=current_user.id).all()
    user = User.query.filter_by(username=uname).first()

    return render_template('profile/profile.html', name=current_user.username, email=current_user.email, password=current_user.password, user=user, pitch=pitch)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        return redirect(url_for('.error'))

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))