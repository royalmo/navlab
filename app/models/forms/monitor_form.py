from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import InputRequired, Length
from flask_babel import gettext

class MonitorForm(FlaskForm):
    key = StringField(validators=[InputRequired(), Length(min=3, max=20)], render_kw={"placeholder": gettext("led")})
    title = StringField(validators=[InputRequired(), Length(min=3, max=80)], render_kw={"placeholder": gettext("Navarcles' Arduino: LED")})
    label = StringField(validators=[InputRequired(), Length(max=20)], render_kw={"placeholder": gettext("State")})
    min_value = FloatField(render_kw={"placeholder": gettext("-0.5")})
    max_value = FloatField(render_kw={"placeholder": gettext("1.5")})
    submit = SubmitField(gettext('Submit Monitor'))
