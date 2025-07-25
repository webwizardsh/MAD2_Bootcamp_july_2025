from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from flask_cors import CORS

import application.config as config

from application.data.model import *
from application.security import security, user_datastore

from application.apis.booksAPI import AllBookAPI, BookAPI
from application.apis.RegisterAPI import RegisterAPI
from application.apis.LoginAPI import LoginAPI


app = Flask(__name__)

app.config.from_object(config)
app.app_context().push()

CORS(app, supports_credentials=True)

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response


db.init_app(app)

api = Api(app)
api.init_app(app)

JWTManager(app)

security.init_app(app, user_datastore)

api.add_resource(AllBookAPI, "/api/book")
api.add_resource(BookAPI, "/api/book/<int:book_id>")
api.add_resource(RegisterAPI, "/api/register")
api.add_resource(LoginAPI, "/api/login")


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(port=8081, debug= True)
    
    
    