#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cc
# @Date  :2019-04-12

import os
from datetime import timedelta

from flask import Flask

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.secret_key = 'zhBRxENODp7PqTqWNO7lj7wvgwPEgc'

prefix = 'sqlite:////'

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', prefix + os.path.join(app.root_path, 'ibook.db.sqlite'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.permanent_session_lifetime = timedelta(seconds=60)

from ibook import views, models
