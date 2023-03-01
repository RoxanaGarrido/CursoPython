### Tuples ###

## Diferencias con lista: 
#La tuple es inmutable no se pueden cambiar sus valores
#Tiene menos métodos que las listas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (23, 1.59, "Roxana", "Garrido")
my_other_tuple = (35, 60)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Roxana")) #cuenta cuantas veces hay ese elemento

print(my_tuple.index("Garrido")) #encuentra el indice que concide

#my_tuple[1] = 1.65 #error: tuple does not support item assignment, es inmutable!

print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple

print(my_sum_tuple)

print(my_sum_tuple[3:6]) # slice, imprime entre indices 3 y 6

my_list = list(my_tuple) # si se quieren editar los valores, cambiarlo a list

print(type(my_list))

my_list[0] = "nuevo"
my_list.insert(1, "Azul")

print(tuple(my_list)) #se puede volver a cambiar a tuple

del my_tuple #se carga toda la variable
#print(my_tuple) error, variable no definida