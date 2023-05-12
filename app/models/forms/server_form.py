from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import InputRequired, Length
from flask_babel import gettext

class ServerForm(FlaskForm):
    name = StringField(validators=[InputRequired(), Length(min=3, max=80)], render_kw={"placeholder": gettext("Minecraft Server")})
    image = URLField(validators=[InputRequired(), Length(min=3, max=80)], render_kw={"placeholder": gettext("https://image.com/ssh.png")})
    description = StringField(validators=[Length(max=80)], render_kw={"placeholder": gettext("About Server")})
    starting_cmd = StringField(validators=[Length(min=3, max=80)], render_kw={"placeholder": gettext("systemctl start `command`")})
    stop_cmd = StringField(validators=[Length(min=3, max=80)], render_kw={"placeholder": gettext("systemctl stop `command`")})
    submit = SubmitField(gettext('Submit Service'))
