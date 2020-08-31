#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@desc  : 
@author: Sarah
@file  : __init__.py.py
@time  : 2020/8/28 22:39
"""
from flask import Flask

import settings
from apps.user.view import user_bp
from exts import db, api


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings.config)
    db.init_app(app=app)
    api.init_app(app=app)
    app.register_blueprint(user_bp)
    return app
