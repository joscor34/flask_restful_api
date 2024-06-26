from app.extensions import db
from .models.producto import Producto
from .models.usuarios import User
from flask_jwt_extended import create_access_token
from datetime import timedelta

def inicio_sesion(email, password):
  # Nos asegura que el usuario efectivamente esté registrado en la DB
  user = User.get_user_by_email(email=email)
  # Tiempo en el que el token expira
  caducidad = timedelta(minutes=2)
  # Si user no es None YYYYYY la contraseña hasheada coincide con la DB 
  if user and (user.check_password(password=password)):
    # Creamos un token de acceso
    token_acceso = create_access_token(identity = user.username, expires_delta = caducidad)
    return { 'Mensaje': 'Loggeado',
             'Token': token_acceso 
          }, 200

  return {'Error': 'El correo o la contraseña no existen :( '}, 400


def user_register(username, email, password):
  # Busca un usuario por su email
  user = User.get_user_by_email(email=email)

  # Si el usuario ya estaba registrado, regresamos un error
  if user is not None:
    return { 'Error': 'Este correo ya está registrado :(' }, 403    


  # Se crea un objeto de tipo 'User' con el username y el correo
  nuevo_usuario = User(username=username, email=email)
  # A ese objeto se le asigna una contraseña
  nuevo_usuario.set_password(password=password) # <- Crearle una contraseña cifrada
  # Guardamos el user en la DB
  nuevo_usuario.save()

  return { 'Nuevo usuario': {
      'email': email,
      'username': username
    } 
  }, 200 # Le damos una respuesta satisfactoria al usuario



# Esta función busca un elemento en la DB por ID o por nombre
def buscar_elemento_id_nombre(parametro_id, parametro_nombre):
  # Verificar si el usuario mando como Query el id
  if parametro_id != None:
    # Obtenemos el producto desde nuestra DB a través del ID
    producto_obtenido = Producto.query.get_or_404(parametro_id)
    # Creamos un JSON donde mostramos los datos del elemento
    json_retornado = {
      'ID': producto_obtenido.id,
      'Nombre': producto_obtenido.nombre,
      'Cantidad': producto_obtenido.cantidad
    }
    # Retornamos ese JSON para que el usuario lo vea
    return json_retornado

  # Verificar si el usuario mandó como Query el nombre
  elif parametro_nombre != None:
    # Buscamos un producto por su nombre y mostramos el primero o 404
    producto_obtenido = Producto.query.filter_by(nombre=parametro_nombre).first_or_404()
    # Creamos un JSON con la info obtenida
    json_retornado = {
      'ID': producto_obtenido.id,
      'Nombre': producto_obtenido.nombre,
      'Cantidad': producto_obtenido.cantidad
    }
    # Retornamos ese JSON para que el usuario lo vea
    return json_retornado

  else:
    return {'Error': 'No pusiste ninguna Query'}, 404
  

def crear_producto(nombre, cantidad):
  nuevo_producto = Producto(nombre=nombre, cantidad=cantidad)
  db.session.add(nuevo_producto)
  db.session.commit()
  json_retornado = {
    'ID': nuevo_producto.id,
    'Nombre': nuevo_producto.nombre,
    'Cantidad': nuevo_producto.cantidad
  }
    # Retornamos ese JSON para que el usuario lo vea
  return json_retornado