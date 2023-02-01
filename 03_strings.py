###Strings###

my_string = "Mi String"
my_other_string = "Mi Other String"


print("Este string tiene", len(my_string), "carateres dentro de la variable") #cuenta el contenido de la VARIABLE

print(my_string + ":" + my_other_string)

my_new_line_string = "Este es un String\n con salto de línea\ty separado por tabulación"
print(my_new_line_string)


name = input("¿Cuál es tu nombre?")
print("¡Bienvenido señor:\n" + name + "!")
print("¡" + name, "está escapando\\de la casa!") #imprime la barra \

surname = input("¿Cuál es tu apellido?")

# Formateo
print("Mi nombre es {} {}" .format(name, surname)) #imprimir el ojeto
print("Mi nombre es %s %s" %(name, surname)) #numero formateado
print(f"Mi nombre es {name} {surname}") #imprimir el ojeto

# Desempaquetado de caracteres
language = "pythOnp"
a, b, c, d, e, f, g = language
print("Normal:",language)
print(a, e)

#División
languaje_slice = language[1:3]#El 1 y el 3
print(languaje_slice)
languaje_slice2 = language[1:]#Desde el 1 hasta el... 
print(languaje_slice2)
languaje_slice3 = language[-2]#2 hacia la izquierda
print(languaje_slice3)
languaje_slice4 = language[0:6:2]#Un salto rebuscadisimo, NO busca lo definido
print(languaje_slice4)

#Reverse
reversed_language = language[ ::-1]
print(reversed_language)


#Funciones
print(language.capitalize())
print(language.upper())
print(language.count("p"))
print(language.isnumeric())#pregunta
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())#Comprueba si está en mayúsculas
print(language.startswith("py"))
print("Py" == "py")







###"\n¡Oh, no!")