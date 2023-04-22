from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import login_user, login_required, logout_user, current_user #############

from ..extensions import db, bcrypt
from ..models import User, LoginForm, RegisterForm

app = Blueprint('users', __name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                if user.active:
                    login_user(user)
                    return redirect(url_for('main.dashboard'))
                return render_template('pages/users/login.html.j2', form=form, inactive_account=True)
    # If POST method, it means that user failed to log in
    return render_template('pages/users/login.html.j2', form=form, bad_credentials=request.method=='POST')

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
        new_user = User(name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return render_template('pages/users/signup_success.html.j2', name=form.name.data)

    return render_template('pages/users/signup.html.j2', form=form, email_taken=request.method=='POST')

@app.route('/userslist', methods=['GET'])
@login_required
def userslist():
    if current_user.admin:
        users = User.query.all()
        #users_time=[]
        #for user in users:
            #last_seen = datetime.now()
            #users_time.append([user,last_seen.strftime('%Y-%m-%d %H:%M:%S.%f')[:-10]])
        return render_template('pages/userlist.html.j2', userlist=users)

    return render_template('pages/userlist.html.j2', not_admin=True)

@app.route('/userslist/delete/<int:id>')
@login_required
def delete(id):
    if current_user.admin:
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('.userslist'))