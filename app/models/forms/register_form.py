from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_babel import gettext

from ...extensions.babel import get_locales
from ..user import User

class RegisterForm(FlaskForm):
    name = StringField(validators=[InputRequired(), Length(min=4, max=80)], render_kw={"placeholder": gettext("User Name")})
    email = EmailField(validators=[InputRequired(), Length(min=4, max=80)], render_kw={"placeholder": gettext("user@example.com")})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": gettext("••••••••")})
    password_confirm = PasswordField(validators=[], render_kw={"placeholder": gettext("••••••••")})
    language = SelectField(choices=get_locales)
    submit = SubmitField(gettext('Register'))

    def validate_email(self, email):
        existing_user_email = User.query.filter_by(email=email.data).first()
        if existing_user_email:
            raise ValidationError(gettext('That email already exists. Please choose a different one.'))
