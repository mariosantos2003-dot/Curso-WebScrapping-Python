
#crear diccionario vacio
diccionario ={}
#print(diccionario)


#asignar valores al diccionario

diccionario["nombre"] = "Mario"
diccionario["edad"] = "20"
print(diccionario)

#obtener valor vinculado a llave
#print(diccionario["nombre"])
#print(diccionario.get("nombre"))

#crear diccionario con valores
diccionario2 = {5.1 :10, "vocales": ["a","e"], (7,2):50}

#numero de elementos(llaves) en el diccionario
print(len(diccionario2))

#eliminar llaves
del(diccionario2["vocales"])
print(diccionario2)