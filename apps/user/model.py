#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@desc  : 
@author: Sarah
@file  : model.py
@time  : 2020/8/29 15:08
"""
from datetime import datetime

from exts import db


class User(db.Model):
    """用户表"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    hobby = db.Column(db.String(30))
    icon = db.Column(db.String(300))
    is_delete = db.Column(db.Boolean())
    email = db.Column(db.String(200))
    rdatetime = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.username