class Usuario:
    def __init__(self, nombre, correo, telefono):
        self.nombre=nombre
        self.correo=correo
        self.telefono=telefono

    def get_nombre(self):
        return self.nombre
    
    def get_correo(self):
        return self.correo
    
    def get_telefono(self):
        return self.telefono
    
class Mensaje:
    def __init__(self, remitente, destinatario, asunto, contenido):
        self.remitente=remitente
        self.destinatario=destinatario
        self.asunto=asunto
        self.contenido=contenido
    
    def get_remitente(self):
        return self.remitente
    
    def get_destinatario(self):
        return self.destinatario
    
    def get_asunto(self):
        return self.asunto
    
    def get_contenido(self):
        return self.contenido
    
class Estacion:
    def __init__(self, nombre, ubicacion, linea):
        self.nombre=nombre
        self.ubicacion=ubicacion
        self. linea=linea

    def get_nombre(self):
        return self.nombre
    
    def get_ubicacion(self):
        return self.ubicacion
    
    def get_linea(self):
        return self.linea
    
class Linea:
    def __init__(self, nombre, color, estaciones):
        self.nombre=nombre
        self.color=color
        self.estaciones=estaciones

    def get_nombre(self):
        return self.nombre
    
    def get_color(self):
        return self.color
    
    def get_estaciones(self):
        return self.estaciones

class Contacto:
    def __init__(self, nombre, correo, mensaje):
        self.nombre=nombre
        self.correo=correo
        self.mensaje=mensaje

    def get_nombre(self):
        return self.nombre
    
    def get_correo(self):
        return self.correo
    
    def get_mensaje(self):
        return self.mensaje
