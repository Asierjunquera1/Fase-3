from flask import Blueprint, render_template


contactos= Blueprint("contactos", __name__)

@contactos.route("/")
def home():
    return render_template("index.html")

@contactos.route("/formulario")
def add_contact():
    return render_template("formulario.html")



 