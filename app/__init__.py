# Importamos la librearía Flask
from flask import Flask
from flask_restful import Api
from .routes import APIRoutes


# Creamos una función para montar el servidor
def crear_app():
  # La variable app contendrá todo nuestro servidor
  app = Flask(__name__)

  # La variable API manejará todas las peticiones hacia nuestro servir
  api = Api(app)
  # Agregamos una variable va a manejar las rutas
  routes = APIRoutes()
  # Inicializamos las rutas en nuestra API
  routes.init_routes(api)


  # Regresamos ese servidor montado
  return app