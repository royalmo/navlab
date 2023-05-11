from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length
from flask_babel import gettext

from ...extensions.babel import get_locales

class LoginForm(FlaskForm):
    email = EmailField(validators=[InputRequired(), Length(min=4, max=80)], render_kw={"placeholder": gettext("user@example.com")})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": gettext("••••••••")})
    remember = BooleanField(gettext('Keep me logged in'))
    submit = SubmitField(gettext('Log In'))