from flask import jsonify
import secrets
from flask_restful import Resource, reqparse


from werkzeug.security import generate_password_hash, check_password_hash

from application.data.model import db,Users, Roles


user_post_args = reqparse.RequestParser()
user_post_args.add_argument("name" , type = str, required = True, help = "name is required")
user_post_args.add_argument("email" , type = str, required = True, help = "email is required")
user_post_args.add_argument("password" , type = str, required = True, help = "password is required")
user_post_args.add_argument("role" , type = str, required = True, help = "role is required")


class RegisterAPI(Resource):
    def post(self):
        args = user_post_args.parse_args()
        name =  args.get("name")
        email =  args.get("email")
        password =  args.get("password")
        role =  args.get("role")
        
        user = Users.query.filter_by(email =email).first()
        
        if user:
            return jsonify({'status':"failed", "message":"user email already registered"})
        user_role = Roles.query.filter_by(name = role).first()
        if user_role is None:
            return jsonify({'status':"failed", "message":"role not exist"})
        
        hash_password = generate_password_hash(password)
        
        new_user = Users(name = name, email=email, password = hash_password)
        new_user.role_id = user_role.id
        new_user.fs_uniquifier = secrets.token_hex(16)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({"status":"success", "message": "user has been registered"})
