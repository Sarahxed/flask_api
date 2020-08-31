#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@desc  : 
@author: Sarah
@file  : view.py
@time  : 2020/8/29 15:09
"""
import os

from flask import Blueprint, url_for
from flask_restful import Resource, marshal_with, fields, reqparse, inputs
from werkzeug.datastructures import FileStorage

from apps.user.model import User
from exts import api, db
from settings import config

user_bp = Blueprint('user', __name__, url_prefix='/api')


user_fields = {
    'username': fields.String,
    'password': fields.String,
    'phone': fields.String,
    'rdatetime': fields.DateTime
}

parser = reqparse.RequestParser()
# location=['form'] 表示只能是post提交
parser.add_argument('username', type=str, required=True, help="用户名必须填写", location=['form'])
parser.add_argument('password', type=inputs.regex(r'^\d{6,12}$'), required=True, help='密码必须6~12位数字', location=['form'])
parser.add_argument('phone', type=inputs.regex(r'^1[3456789]\d{9}$'), required=True, help="手机号必须填写", location=['form'])
parser.add_argument('hobby', action='append')  # 多选值
parser.add_argument('icon', type=FileStorage, location=['files'])


class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self):
        users = User.query.all()
        return users

    @marshal_with(user_fields)
    def post(self):
        args = parser.parse_args()
        username = args.get('username')
        password = args.get('password')
        phone = args.get('phone')
        hobby = args.get('hobby')
        icon = args.get('icon')
        user = User()
        if icon:
            upload_path = os.path.join(config.UPLOAD_ICON_DIR,icon.filename)
            icon.save(upload_path)
            user.icon = config.UPLOAD_ICON_DIR + '\\' + icon.filename
        user.username = username
        user.password = password
        user.phone = phone
        db.session.add(user)
        db.session.commit()
        return user

    def put(self):
        pass


class UserResourceSimple(Resource):
    @marshal_with(user_fields)
    def get(self, uid):
        user = User.query.get(uid)
        return user

    def post(self, uid):

        pass

    def put(self, uid):
        print('endpoint使用：', url_for('user_all'))
        return {'code': 200, 'msg': "ok"}


api.add_resource(UserResource, '/user', endpoint="user_all")
api.add_resource(UserResourceSimple, '/user/<string:uid>')

