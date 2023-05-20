from flask import Flask
from routes.contactos import contactos


app=Flask(__name__)


app.register_blueprint(contactos)

