# Importamos la librearía Flask
from flask import Flask
from flask_restful import Api
from .routes import APIRoutes
from .config import Config
from .extensions import db

# Creamos una función para montar el servidor
def crear_app():
  # La variable app contendrá todo nuestro servidor
  app = Flask(__name__)
  # Le indicamos a nuestra app que se configura a través de un objeto

  # Se iba a configurar a través de un objeto
  app.config.from_object(Config)

  # Conectamos la App con la base de datos
  db.init_app(app)
  
  # Antes de que se cree el acceso a la API, 
  # se ejecuta primero esto
  with app.app_context():
    # Inicializamos la DB
    db.create_all()

    # La variable API manejará todas las peticiones hacia nuestro servir
    api = Api(app)
    # Agregamos una variable va a manejar las rutas
    routes = APIRoutes()
    # Inicializamos las rutas en nuestra API
    routes.init_routes(api)

  # Regresamos ese servidor montado
  return app