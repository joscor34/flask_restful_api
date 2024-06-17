from app.extensions import db
from .models.producto import Producto

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