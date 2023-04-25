from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField

class SearchForm(FlaskForm):
    search = StringField(render_kw={"placeholder": "Search"})