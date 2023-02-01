### Lists ###

#constructores
my_list = list(); 
my_other_list = []; 

print(len(my_list)); #len largo de la lista

my_list = [35,24,62,52,30,17]; #lista de números

print(my_list); #imprimir los objetos de la lista
print(len(my_list));

my_other_list = [35,1.77,"Brais", "Moure"]; #lista de varios tipos

print(type(my_other_list));

print(my_other_list[0]); #acceder a una posición

print(my_other_list[-1]); #último elemento (va dando la vuelta) 1 sola vez**

#print(my_other_list[-5]); #index out of range

print(my_other_list.count("Brais")); #count número de ocurrencias de un elemento


#desempaquetado
age, height, name, surname = my_other_list; #igualar variables con las posiciones

print(name) 

print(my_list + my_other_list) #concatenar listas

print(list([1,2,3])) #imprime lo mismo
print([1,2,3])

my_other_list.append("MoureDev"); #append inserta nuevo elemento al final
print(my_other_list);

my_other_list.insert(1, "Azul"); #agregar elemento en index 

my_other_list.remove("Azul"); #elimina el primer elemento que coincide

my_list.pop(); #elimina el último elemento (también lo devuelve)

my_list.pop(2); #elimina el elemento del index

del my_list[2]; #eliminar elemento de la lista por índice

my_new_list = my_list.copy(); #copia la lista en otra variable

my_list.clear(); #borra la lista entera

my_new_list.reverse(); #invierte la lista
print(my_new_list)

my_new_list.sort(); #ordena de mayor a menor por defecto

my_new_list[1:2]; #slice para hacer sublistas











