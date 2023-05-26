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






 