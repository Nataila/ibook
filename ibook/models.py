#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cc
# @Date  :2019-04-11

from datetime import datetime

from sqlalchemy_utils import ChoiceType
from werkzeug.security import generate_password_hash, check_password_hash

from .utils import db


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

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def valid_password(self, password):
        return check_password_hash(self.password, password)


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
