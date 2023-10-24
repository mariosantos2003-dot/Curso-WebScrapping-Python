
cadena = "hola"

cadena_corta ="adios amore"

#multiplicar cadena
print(cadena*2)

#el numero entre [] se refiere a cada letra de la cadena
print(cadena_corta[0])

#letras de la 0 a la 5
print(cadena_corta[0:5])

#ultima letra
print(cadena[-1])


#metodos de cadenas

#longitud de letras de la cadena(incluyendo espacios)
print(len(cadena))

#devuelve la primera posicion de la letra que le pases
print(cadena_corta.find("a"))


#devuelve la ultima posicion de la letra que le pases
print(cadena_corta.rfind("a"))


#convertir a minusculas
print(cadena_corta.lower())
#convertir a mayusculas
print(cadena_corta.upper())
#convertir a primera letra
print(cadena_corta.capitalize())

#remplazar  caracteres
print(cadena_corta.replace("a", "1",2))


#compobar minisculas o mayusculas
print(cadena_corta.islower())
print(cadena_corta.isupper())
