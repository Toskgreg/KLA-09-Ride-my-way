from flask_jwt_extended import JWTManager
from flask_restplus import Api

from v1 import create_app, register_blueprints

app = create_app('development')  # create the Flask Instance
# api instance is instantiated
api = Api(app, version='1', title='Ride-My-Way API', description="The rides API for my carpooling application")
# register blueprints
register_blueprints(app=app)

# configure JWT
app.config['JWT_SECRET_KEY'] = '$pbkdf2-sha256$29000$I.T8f8/ZG8M4J0QIwTgHIA$.9wCvRZECxd7/yvHttEgoHzpvgjdhjizq5ySewKfeQc'
jwt = JWTManager(app)


if __name__ == '__main__':
    app.run()
