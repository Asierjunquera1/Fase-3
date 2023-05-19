from flask import Blueprint

lineas= Blueprint("lineas", __name__)

@lineas("/")
def home():
    return "Lineas de metro"
