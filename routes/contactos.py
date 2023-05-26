from flask import Blueprint, render_template, request, redirect, url_for



contactos= Blueprint("contactos", __name__)

@contactos.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('enviar'))
    
    return render_template("index.html")

    

@contactos.route("/enviar")
def enviado():
    return render_template("formulario_enviado.html")

@contactos.route("/about")
def about():
    return render_template("about.html")

@contactos.route("/preguntas_frecuentes")
def preguntas_frecuentes():
    return render_template("preguntas_frecuentes.html")

contactos.route("/servicios")
def servicios():
    return render_template("servicios.html")








 