#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cc
# @Date  :2019-04-11

import os
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import ChoiceType

app = Flask(__name__)

prefix = 'sqlite:////'

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', prefix + os.path.join(app.root_path, 'ibook.db.sqlite'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'hello'


# Models
class User(db.Model):
    '''
    用户表
    '''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    bills = db.relationship('Bill')
    created_at = db.Column(db.DateTime, default=datetime.now)


class Bill(db.Model):
    '''
    账单表
    '''
    TAG_CHOICES = (
        (1, '购物'),
        (2, '蔬菜'),
    )
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.Float)
    remark = db.Column(db.String(50))
    tag = db.Column(ChoiceType(TAG_CHOICES, db.Integer()))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.now)


@app.cli.command()
def initdb():
    '''init db'''
    db.create_all()
    print('initialized database')


if __name__ == "__main__":
    app.run(debug=True)
