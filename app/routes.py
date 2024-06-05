# Importamos el modulo "Resource" de la librería flask_restful
from flask_restful import Resource # <- Es un clase
# El modulo request nos permite aceptar info de un usuario
from flask import request, jsonify
# Importamos los métodos de nuestra API
from .methods import *



lista_objetos_almacen = [
{
  'id':1,
  'nombre': 'Lapiz',
  'cantidad': 4
},
{
  'id':2,
  'nombre': 'Goma',
  'cantidad': 3
},
{
  'id':3,
  'nombre': 'Tijera',
  'cantidad': 6
}
]


# Creamos una clase que va a heredar atributos del modulo "Resource"
class HelloWorld(Resource):
  # Este método se va a ejecutar cuando el usuario acceda a cierta ruta a través del método GET  
  def get(self):
    # Regresarnos un diccionario con el mensaje que queremos mostrar
    return { 'message': 'Hola mundo desde la API', 'status':200 }



class Almacen(Resource):
  # Obtenemos la información del almacén
  # Le pedimos información a la ruta por medio de un GET
  def get(self):
    # Esta variable va a interceptar la informacion de nuestra Query
    parametro_id = request.args.get('id')
    parametro_nombre = request.args.get('nombre')

    return buscar_elemento_id_nombre(lista_objetos_almacen, parametro_id, parametro_nombre)
  # Ponemos un nuevo objeto en el almacén
  # Enviarle informacion a la API mediante el cliente
  def post(self):
    # Se crea una nueva variable para guardar la información que Posteo el ususario
    data = request.get_json()

    #Agregamos la informacion a lista del almacen
    lista_objetos_almacen.append(data)

    return { 'received': True, 'status':200, 'info':data }


# Creamos una clase que va a manejar todas las rutas
class APIRoutes():
  # Se declara un método para inicializar las ruta
  def init_routes(self, api):
    # Agregamos una nueva ruta a nuestra API
    api.add_resource(HelloWorld, '/')
    
    # Agregamos un nuevo recurso
#                   Recurso,  Ruta donde esta el recurso
    api.add_resource(Almacen, '/objetos_almacen')

