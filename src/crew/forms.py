from flask              import current_app
from flask_wtf          import FlaskForm
from wtforms            import StringField,SubmitField,SelectField,TextAreaField,HiddenField
from wtforms.widgets    import TextArea
from wtforms.validators import DataRequired

class crewMember(FlaskForm):
    username   = StringField("Usename",[DataRequired("Username required")])
    email      = StringField("E-mail")
    first_name = StringField("First Name",[DataRequired("First name required")])
    last_name  = StringField("Last Name",[DataRequired("Last name required")])
    nickname   = StringField("Nickname")
    rank       = StringField("Rank",[DataRequired("Rank required")])
    submit     = SubmitField()

class selectCrewMember(FlaskForm):
    username = SelectField("Crew member")
    submit   = SubmitField()
