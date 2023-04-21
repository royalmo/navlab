from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    email = EmailField(validators=[InputRequired(), Length(min=4, max=80)], render_kw={"placeholder": "user@example.com"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "••••••••"})
    submit = SubmitField('Login')
