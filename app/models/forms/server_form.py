from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import InputRequired, Length, ValidationError

class ServerForm(FlaskForm):
    name = StringField(validators=[InputRequired(), Length(min=3, max=80)], render_kw={"placeholder": "Minecraft Server"})
    image = URLField(validators=[InputRequired(), Length(min=3, max=80)], render_kw={"placeholder": "https://image.com/ssh.png"})
    description = StringField(validators=[InputRequired(), Length(min=0, max=20)], render_kw={"placeholder": "About Server"})
    starting_cmd = StringField(validators=[InputRequired(), Length(min=3, max=80)], render_kw={"placeholder": "systemctl start `command`"})
    stop_cmd = StringField(validators=[InputRequired(), Length(min=3, max=80)], render_kw={"placeholder": "systemctl stop `command`"})
    status_cmd = StringField(validators=[InputRequired(), Length(min=3, max=80)], render_kw={"placeholder": "systemctl status `command`"})
    submit = SubmitField('Submit Service')
