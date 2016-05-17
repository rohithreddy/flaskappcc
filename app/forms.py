import wtforms
from wtforms import validators
from models import Person


class LoginForm(wtforms.Form):
    email = wtforms.StringField("Email", validators=[validators.data_required()])
    password = wtforms.PasswordField("Password",validators=[validators.DataRequired])
    remember_me = wtforms.BooleanField("Remember me?",default=True)

    def validate(self):
        if not super(LoginForm,self).validate():
            return False

        self.person = Person.authenticate(self.email.data, self.password.data)

        if not self.person:
            self.email.errors.append("Invalid email address or Password")
            return False
        return True
