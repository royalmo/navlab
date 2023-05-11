from flask_wtf import FlaskForm
from wtforms import SelectField

from ...extensions.babel import get_locales

class SelectForm(FlaskForm):
    language = SelectField(choices=get_locales)