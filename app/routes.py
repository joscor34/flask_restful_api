# Importamos el modulo "Resource" de la librería flask_restful
from flask_restful import Resource
# El modulo request nos permite aceptar info de un usuario
from flask import request, jsonify
# Convierte la info de texto a un diccionario
from urllib.parse import parse_qs

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
  def get(self):
    return { 'Objetos': lista_objetos_almacen, 'status':200 }

  # Ponemos un nuevo objeto en el almacén
  def post(self):
    # Se crea una nueva variable para guardar la información que Posteo el ususario
    data = request.get_data(as_text=True)
    # Parseamos la data
    parsed_data = parse_qs(data)
    # Convertimos de diccionario "Raro" a JSON
    json_data = {k: v[0] for k, v in parsed_data.items()}


    print(json_data)
    #Agregamos la informacion a lista del almacen
    #lista_objetos_almacen.append(data)

    return { 'received': True, 'status':200 }



# Creamos una clase que va a manejar todas las rutas
class APIRoutes():
  # Se declara un método para inicializar las ruta
  def init_routes(self, api):
    # Agregamos una nueva ruta a nuestra API
    api.add_resource(HelloWorld, '/')
    
    # Agregamos un nuevo recurso
    api.add_resource(Almacen, '/objetos_almacen')

