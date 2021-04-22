from firstapp import app
from flask import render_template, flash
from firstapp.forms import AddUser
from firstapp.models import User
from firstapp import db

@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/adduser', methods=['GET','POST'])
def adduser_page():
    form = AddUser()
    if form.is_submitted():
        return 'Yea'
    return render_template('adduser.html', form=form)

