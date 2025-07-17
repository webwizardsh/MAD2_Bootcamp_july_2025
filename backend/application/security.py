from flask_security import Security, SQLAlchemyUserDatastore


from .data.model import db, Users,Roles

user_datastore = SQLAlchemyUserDatastore(db,Users,Roles)

security = Security()
