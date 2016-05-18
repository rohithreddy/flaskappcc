from flask import flash, redirect, render_template, request, url_for
from flask.ext.login import login_user

from app import app,db
from app import login_manager
from forms import LoginForm, RegisterForm, RechargeForm

from models import Person, Recharge


@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form = LoginForm(request.form)
        if form.validate():
            login_user(form.user, remember = form.remember_me.data)
            flash("Successfully logged in as %s" % form.user.email, "success")
            return redirect(request.args.get("next") or url_for("homepage"))
    else:
        form = LoginForm()
        return render_template("login.html", form=form)


@app.route('/register', methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        form = RegisterForm(request.form)
        if form.validate():
            person = Person.create(
                email=form.email.data,
                password=form.password.data,
                dob=form.dob.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                phone_no=form.phone_no.data
            )
            db.session.add(person)
            db.session.commit()
            flash("Successfully registered as %s" % form.email.data, "success")
            return render_template("login.html")
            redirect("login")
        else:
            form = RegisterForm()
            return render_template("register.html", form=form)
    else:
        form = RegisterForm()
        return render_template("register.html", form=form)


@app.route('/recharge', methods=["GET", "POST"])
def recharge():
    if request.method == "POST":
        form = RechargeForm(request.form)
        if form.validate():
            recharge = Recharge(phone_no=form.phone_no.data, email_id=form.email_id.data, recharge_type=form.recharge_type.data, amount=form.amount.data)
            db.session.add(recharge)
            db.session.commit()
            flash("Recharge Success for Mobile Number %s" % form.phone_no.data, "success")
            redirect("homepage")
            return render_template("homepage.html")
    else:
        form = RechargeForm()
        return render_template("recharge.html", form=form)
