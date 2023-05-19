from flask import Blueprint, render_template, url_for, redirect, request, make_response
from flask_login import login_user, logout_user, current_user
from flask_babel import gettext,get_locale

from ..extensions import db, bcrypt, login_required, mailer, admin_required
from ..models import User, LoginForm, RegisterForm, SearchForm, SelectForm, UserForm
from jinja2 import utils
app = Blueprint('users', __name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # If user is already logged in
    if current_user.is_authenticated:
        return redirect(request.args.get('next') if request.args.get('next') else url_for('main.dashboard'))

    sel=SelectForm()
    sel.language.default=get_locale()
    sel.process()

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                if user.active:
                    login_user(user, remember=form.remember.data)
                    return redirect(request.args.get('next') if request.args.get('next') else url_for('main.dashboard'))
                return render_template('pages/users/login.html.j2', form=form, inactive_account=True, title=gettext('Log In'),sel=sel)
    # If POST method, it means that user failed to log in
    return render_template('pages/users/login.html.j2', form=form, bad_credentials=request.method=='POST', title=gettext('Log In'),sel=sel)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    # If user is already logged in
    if current_user.is_authenticated: return redirect(url_for('main.dashboard'))

    form = RegisterForm()

    if form.validate_on_submit() and form.password.data == form.password_confirm.data:
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(name=str(utils.escape(form.name.data)), email=str(utils.escape(form.email.data)), password=hashed_password, lang=str(utils.escape(form.language.data)))
        db.session.add(new_user)
        db.session.commit()
        mailer.new_user(new_user)
        return redirect(url_for('.register_success', lang=form.language.data))
    
    form.language.default=get_locale()
    form.process()

    return render_template('pages/users/signup.html.j2', form=form, email_taken=request.method=='POST', title=gettext('Register'))

@app.route('/register/success')
def register_success():
    # If user is already logged in
    if current_user.is_authenticated: return redirect(url_for('main.dashboard'))

    return render_template('pages/users/signup_success.html.j2', title=gettext('Registered!'))

@app.route('/users')
@admin_required
def users():
    search_form = SearchForm(request.form)
    search_query = request.args.get('search')
    if search_query:
        users = User.query.filter(User.name.contains(search_query)).all()
    else:
        users = User.query.all()
    
    return render_template('pages/userlist.html.j2',
                            userlist=users,
                            search_form=search_form,
                            navbar_highlight_users=True,
                            title=gettext('Users'))

@app.route('/users/<int:user_id>', methods=['DELETE'])
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return make_response("No content", 204)

@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = UserForm()

    if form.validate_on_submit():
        user.update_with_form(form, current_user.admin)
        return redirect(url_for('.users'))

    form.language.default=user.lang
    form.process()
    return render_template('pages/newuser.html.j2', user=user, form=form, title=gettext('Edit user'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user = current_user
    form = UserForm()

    if form.validate_on_submit():
        user.update_with_form(form, current_user.admin)
        return redirect(url_for('.profile'))

    form.language.default=user.lang
    form.process()
    return render_template('pages/newuser.html.j2', user=user, form=form, navbar_highlight_profile=True, title=gettext('Your Profile'))
