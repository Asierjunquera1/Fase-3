from flask import Blueprint, render_template


contactos= Blueprint("contactos", __name__)

@contactos.route("/")
def home():
    return render_template("index.html")

@contactos.route("/guardar_contacto")
def add_contact():
    return "Guardando contacto"



 