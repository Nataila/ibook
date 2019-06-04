#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cc
# @Date  :2019-05-13


from functools import wraps

from ibook import app
from flask import session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


def login_required(func):
    '''
    login required
    '''
    @wraps(func)
    def decorated(*args, **kwargs):
        if 'username' not in session:
            return 'not login'
        else:
            return func(*args, **kwargs)
    return decorated
