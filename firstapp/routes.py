from firstapp import app
from flask import render_template, flash
from firstapp.forms import AddUser
from firstapp.models import User
from firstapp import db
import random as rand

@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/adduser', methods=['GET','POST'])
def adduser_page():
    form = AddUser()
    if form.is_submitted():
        user_to_add = User(id=rand.randint(1,500),
                        name=form.name.data,
                        address=form.address.data)
        db.session.add(user_to_add)
        db.session.commit()
        return render_template('success.html', userdetails=user_to_add)
    return render_template('adduser.html', form=form)

@app.route('/viewuser',methods=['GET','POST'])
def viewuser_page():
    user = User.query.all()
    return render_template('viewuser.html', user=user)

