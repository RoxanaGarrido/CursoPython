## Sets ##
# No admite repeticiones o duplicados

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Dictionary ?

my_other_set = {"Roxana", "Garrido", 23}

print(type(my_other_set)) # Ahora que tiene elementos es un Set

print(len(my_other_set))

#print(my_other_set[0]) error, set object is not subscriptable

my_other_set.add("nuevo")

print(my_other_set) #No es una estructura ordenada 

my_other_set.add("nuevo") #No funciona si ese elemento ya existe (no se repiten elementos)

#Busca el elemento en el set
print("Roxana" in my_other_set) #True 
print("roxana" in my_other_set) #False

my_other_set.remove("Roxana") #Eliminar elemento

print(my_other_set)

my_other_set.clear() #Borra todos los elementos

print(my_other_set)

del my_other_set # Elimina la variable

my_set = {"nuevo"}
my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set) # Unir dos sets

print(my_new_set)

print(my_new_set.difference(my_set)) # Imprime los elementos de my_new_set menos los de my_set