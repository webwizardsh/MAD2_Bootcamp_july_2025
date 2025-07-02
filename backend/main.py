from flask import Flask
from flask_restful import Api

import application.config as config

from application.data.model import *
from application.security import security, user_datastore

from application.apis.booksAPI import AllBookAPI, BookAPI



app = Flask(__name__)

app.config.from_object(config)
app.app_context().push()

db.init_app(app)

api = Api(app)
api.init_app(app)

security.init_app(app, user_datastore)

api.add_resource(AllBookAPI, "/api/book")
api.add_resource(BookAPI, "/api/book/<int:book_id>")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(port=8081, debug= True)
    
    
    