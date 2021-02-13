from datetime import datetime
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app import db


# from app import login
# from app.search import add_to_index, remove_from_index, query_index
# import simplejson as json
# from flask import jsonify

# class User(UserMixin, db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#     bio = db.Column(db.String(140))
#
#     def __repr__(self):
#         return '<User {}>'.format(self.username)
#
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
#
#     def avatar(self, size):
#         digest = md5(self.email.lower().encode('utf-8')).hexdigest()
#         return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)
#
#     def get_reset_password_token(self, expires_in=600):
#         return jwt.encode(
#             {'reset_password': self.id, 'exp': time() + expires_in},
#             current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')
#
#     @staticmethod
#     def verify_reset_password_token(token):
#         try:
#             id = jwt.decode(token, current_app.config['SECRET_KEY'],
#                             algorithms=['HS256'])['reset_password']
#         except:
#             return
#         return User.query.get(id)
