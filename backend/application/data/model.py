from .database import db
from flask_security import UserMixin, RoleMixin
  

class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True)
    email = db.Column(db.String(80), unique = True, nullable =False)
    password = db.Column(db.String(200), nullable = False)
    fs_uniquifier = db.Column(db.String(300), nullable = False)
    active = db.Column(db.Boolean)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable = False)
    
    role = db.relationship('Roles', backref = db.backref('users'))


    
class Roles(db.Model, RoleMixin):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True)
    
    
class Books(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True)
    author = db.Column(db.String(60))