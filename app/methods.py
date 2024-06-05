def buscar_elemento_id_nombre(lista_objetos_almacen, parametro_id, parametro_nombre):
  
    # Comparamos si le esta llegando un parametro "nombre"
    if parametro_nombre != None:
      for objeto in lista_objetos_almacen:     
        # Si la llave 'id' de un objeto coincide con lo que nos pide el usuiaro
        if (objeto.get('nombre') == parametro_nombre):
          # Regresamos el objeto que pidió
          return { 'Objeto':objeto, 'status':200 }
     # Si no encuentra coincidencia, le da un mensaje de no encontrado
      return { 'Mensaje': 'Objeto no encontrado', 'status':404 } 


    # Comparamos si el parámetro esta vacío 
    elif parametro_id != None:
      # Si el ID existe en nuestra BD
      # Recorremos la lista de objetos en el almacen
      for objeto in lista_objetos_almacen:     
        # Si la llave 'id' de un objeto coincide con lo que nos pide el usuiaro
        if (objeto.get('id') == int(parametro_id)):
          # Regresamos el objeto que pidió
          return { 'Objeto':objeto, 'status':200 }
     # Si no encuentra coincidencia, le da un mensaje de no encontrado
      return { 'Mensaje': 'Objeto no encontrado', 'status':404 }

     
    # Si el parametro no se mandó, regresamos todos los objetos de mi lista
    return { 'Objetos': lista_objetos_almacen, 'status':200 }

