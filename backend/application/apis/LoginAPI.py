from flask import jsonify
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_security import login_user

from flask_jwt_extended import create_access_token

from application.data.model import db,Users, Roles


user_post_args = reqparse.RequestParser()
user_post_args.add_argument("email" , type = str, required = True, help = "email is required")
user_post_args.add_argument("password" , type = str, required = True, help = "password is required")


class LoginAPI(Resource):
    def post(self):
        args = user_post_args.parse_args()
        email =  args.get("email")
        password =  args.get("password")
        
        user = Users.query.filter_by(email =email).first()
        
        if user is None:
            return jsonify({'status':"failed", "message":"user email not registered"})

        if not check_password_hash(user.password, password):
            return jsonify({'status':"failed", "message":"wrong password"})

        access_token = create_access_token(identity = user.email)
        
        login_user(user)
        
        role = Roles.query.filter_by(id = user.role_id).first()
        
        return jsonify({"status":"success", "message": "successfully login", "access_token" :access_token, "email": email, "role":role.name})
