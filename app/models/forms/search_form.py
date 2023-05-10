from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField
from flask_babel import gettext

class SearchForm(FlaskForm):
    search = StringField(render_kw={"placeholder": gettext("Search")})
    submit = SubmitField(gettext("Search"))