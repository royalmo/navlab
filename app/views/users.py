from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import login_user, logout_user, current_user
from flask_babel import gettext

from ..extensions import db, bcrypt, login_required, mailer
from ..models import User, LoginForm, RegisterForm, SearchForm

app = Blueprint('users', __name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                if user.active:
                    login_user(user, remember=form.remember.data)
                    return redirect(request.args.get('next') if request.args.get('next') else url_for('main.dashboard'))
                return render_template('pages/users/login.html.j2', form=form, inactive_account=True, title=gettext('Log In'))
    # If POST method, it means that user failed to log in
    return render_template('pages/users/login.html.j2', form=form, bad_credentials=request.method=='POST', title=gettext('Log In'))

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit() and form.password.data == form.password_confirm.data:
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(name=form.name.data, email=form.email.data, password=hashed_password, lang=form.language.data)
        db.session.add(new_user)
        db.session.commit()
        mailer.new_user(new_user)
        return render_template('pages/users/signup_success.html.j2', name=form.name.data, title=gettext('Registered!'))

    return render_template('pages/users/signup.html.j2', form=form, email_taken=request.method=='POST', title=gettext('Register'))

@app.route('/users')
@login_required
def users():
    if not current_user.admin:
        return redirect('/')

    search_form = SearchForm(request.form)
    search_query = request.args.get('search')
    if search_query:
        users = User.query.filter(User.name.contains(search_query))
    else:
        users = User.query.all()
    
    return render_template('pages/userlist.html.j2',
                            userlist=users,
                            search_form=search_form,
                            navbar_highlight_users=True,
                            title=gettext('Users'))

@app.route('/users/<int:user_id>/delete')
@login_required
def delete_user(user_id):
    if current_user.admin:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('.users'))

@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        user.lang=request.form['language']
        if request.form['password'] and request.form['password']==request.form['password_confirm']:
            user.password = bcrypt.generate_password_hash(request.form['password'])
        user.admin = 'admin' in request.form and current_user.admin
        user.active = 'active' in request.form and current_user.admin
        db.session.commit()
        return redirect(url_for('.users'))
    return render_template('pages/newuser.html.j2', user=user, title=gettext('Edit user'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user = current_user
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        user.lang=request.form['language']
        if request.form['password'] and request.form['password']==request.form['password_confirm']:
            user.password = bcrypt.generate_password_hash(request.form['password'])
        user.admin = 'admin' in request.form and current_user.admin
        user.active = 'active' in request.form and current_user.admin
        db.session.commit()
        return redirect(url_for('.profile'))
    return render_template('pages/newuser.html.j2', user=user, navbar_highlight_profile=True, title=gettext('Your Profile'))
