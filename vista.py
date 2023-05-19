from pyramid.view import view_config
from pyramid.config import Configurator

@view_config(route_name="home")
def home_view(request):
    return{"message": "¡Bienvenido a MetroGo!"}



def includeme(config):
    config.add_route('home', '/')
    config.scan('.views')

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include(includeme)
    return config.make_wsgi_app()
