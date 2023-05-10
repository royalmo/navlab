from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import login_user, logout_user, current_user

from ..extensions import db, bcrypt, login_required
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
        if form.language.data=='English':
            lan='en'
        else:
            lan='ca'
        new_user = User(name=form.name.data, email=form.email.data, password=hashed_password,lang=lan)
        db.session.add(new_user)
        db.session.commit()
        return render_template('pages/users/signup_success.html.j2', name=form.name.data)

    return render_template('pages/users/signup.html.j2', form=form, email_taken=request.method=='POST')

@app.route('/userslist', methods=['GET'])
@login_required
def userslist():
    
    search_form = SearchForm(request.form)
    search_query = request.args.get('search')

    if current_user.admin:
        if request.method == 'GET' and search_query:
            users = User.query.filter(User.name.contains(search_query))
        else:
            users = User.query.all()
        
        return render_template('pages/userlist.html.j2',
                               userlist=users,
                               search_form=search_form,
                               navbar_highlight_users=True)

    return redirect('/')

@app.route('/userslist/delete/<int:id>')
@login_required
def delete(id):
    if current_user.admin:
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('.userslist'))

@app.route('/userslist/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        if request.form['password'] and request.form['password']==request.form['password_confirm']:
            user.password = bcrypt.generate_password_hash(request.form['password'])
        if request.form['language']=='English':
            user.lang='en'
        elif request.form['language']=='Catalan':
            user.lang='ca'
        user.admin = 'admin' in request.form
        user.active = 'active' in request.form
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('pages/newuser.html.j2', user=user, navbar_highlight_profile=True)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return redirect('/userslist/edit/'+str(current_user.id))


