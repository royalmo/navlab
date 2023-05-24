from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, SelectField, BooleanField
from wtforms.validators import InputRequired, Length
from flask_babel import gettext

from ...extensions.babel import get_locales

class UserForm(FlaskForm):
    name = StringField(validators=[InputRequired(), Length(min=4, max=80)], render_kw={"placeholder": gettext("User Name")})
    email = EmailField(validators=[InputRequired(), Length(min=4, max=80)], render_kw={"placeholder": gettext("user@example.com")})
    password = PasswordField(render_kw={"placeholder": gettext("••••••••")})
    password_confirm = PasswordField(validators=[], render_kw={"placeholder": gettext("••••••••")})
    language = SelectField(choices=get_locales)
    submit = SubmitField(gettext('Register'))
    admin = BooleanField(gettext('Admin?'))
    active = BooleanField(gettext('Active?'))
