#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cc
# @Date  :2019-04-11

from flask import request, session

from ibook import app
from .utils import login_required, db
from .models import User


@app.route('/')
def index():
    if 'username' in session:
        return 'hello, {}'.format(session['username'])
    return 'hello'


@app.route('/login', methods=['POST'])
def login():
    if session.get('username'):
        return 'has logined'
    username, password = map(request.form.get, ['username', 'password'])
    user = User.query.filter_by(username=username).first()
    if not user:
        return 'User Does not exists'
    if not user.valid_password(password):
        return 'Password is not valid'
    session['username'] = username
    session.permanent = True
    return 'login ed'


@app.route('/register', methods=['POST'])
def register():
    username, password = map(request.form.get, ('username', 'password'))
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return 'reg'


@app.route('/name')
@login_required
def get_name():
    return 'chen'


@login_required
@app.route('/logout', methods=['POST'])
def logout():
    if 'username' in session:
        session.pop('username')
    return 'logout success'


@login_required
@app.route('/bill/new', methods=['POST'])
def bill_new():
    pass


@app.cli.command()
def initdb():
    '''init db'''
    db.create_all()
    print('initialized database')


if __name__ == "__main__":
    app.run(debug=True)
