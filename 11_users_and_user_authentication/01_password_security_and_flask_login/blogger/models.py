from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime
from blogger import app

db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, index=True)
    email = db.Column(db.String(50), unique=True, index=True)
    dateofreg = db.Column(db.DateTime, default=datetime.datetime.now)
    passwordhash = db.Column(db.String(128))

    def get_id(self):
        return str(self.uid)

    @property
    def password(self):
      raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
      self.passwordhash = generate_password_hash(password)

    def verify_password(self, password):
      return check_password_hash(self.passwordhash, password)

    def __repr__(self):
      return f"<User {self.username}>"

    # @login_manager.user_loader
    # def load_user(user_id):
    # return User.query.get(int(user_id))

    def __init__(self, firstname, lastname, username, password, email):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email


class Post(db.Model):
    __tablename__ = 'posts'
    pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    puid = db.Column(db.Integer, db.ForeignKey('users.uid'))

    def __init__(self, title, description, puid):
        self.title = title
        self.description = description
        self.puid = puid
