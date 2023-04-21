from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length, ValidationError

from ..user import User

class RegisterForm(FlaskForm):
    name = StringField(validators=[InputRequired(), Length(min=4, max=80)], render_kw={"placeholder": "Taylor Swift"})
    email = EmailField(validators=[InputRequired(), Length(min=4, max=80)], render_kw={"placeholder": "user@example.com"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "••••••••"})
    password_confirm = PasswordField(validators=[], render_kw={"placeholder": "••••••••"})
    submit = SubmitField('Register')

    def validate_email(self, email):
        existing_user_email = User.query.filter_by(email=email.data).first()
        if existing_user_email:
            raise ValidationError('That email already exists. Please choose a different one.')
