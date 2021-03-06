import wtforms
from wtforms import validators
from models import Person, Recharge
from views import g


class LoginForm(wtforms.Form):
    email = wtforms.StringField("Email", validators=[validators.DataRequired()])
    password = wtforms.PasswordField("Password", validators=[validators.DataRequired()])
    remember_me = wtforms.BooleanField("Remember me?", default=True)

    def validate(self):
        if not super(LoginForm, self).validate():
            return False
        g.user = Person.authenticate(self.email.data, self.password.data)
        self.user = g.user
        if not self.user:
            self.email.errors.append("Invalid email or password.")
            return False
        return True

class RegisterForm(wtforms.Form):
    first_name = wtforms.StringField("First Name", validators=[validators.DataRequired()])
    last_name = wtforms.StringField("Last Name", validators=[validators.DataRequired()])
    age = wtforms.IntegerField("Age", validators=[validators.DataRequired()])
    email = wtforms.StringField("Email Id", validators=[validators.DataRequired()])
    phone_no = wtforms.StringField("Phone Number", validators=[validators.DataRequired()])
    password = wtforms.PasswordField("Password", validators=[validators.DataRequired(), validators.equal_to("confirm_pass")])
    confirm_pass = wtforms.PasswordField("Confirm Password", validators=[validators.DataRequired()])
    twitter_id = wtforms.StringField("Twitter Screen Name / ID")
    facebook_id = wtforms.StringField("Facebook ID")


class RechargeForm(wtforms.Form):
    phone_no = wtforms.StringField("Mobile number", validators=[validators.DataRequired()])
    email_id = wtforms.StringField("Email id", validators=[validators.DataRequired()])
    recharge_type = wtforms.SelectField("Select Recharge Type", choices=[('VOICE', 'VOICE'), ('DATA', 'DATA'), ('SMS', 'SMS')], validators=[validators.DataRequired()])
    amount = wtforms.IntegerField("Amount", validators=[validators.DataRequired()])
