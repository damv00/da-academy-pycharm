#List operations
'''
append  .append(elemento)
extend  .extend(listanueva)
insert  .insert(posicion,elemento)
del     del lista[]                                                             <-
remove  .remove(elemento)
reverse .reverse()
sort    .sort()     o       .sort(reverse=True)     o   .sort(key=Funcion)
sorted  sorted(lista)       sorted(lista,reverse=true)                          <-
min     min(lista)                                                              <-
max     max(lista)                                                              <-
index   .index(elemento)
count   .count(lista)
sum     .sum(lista)
in
'''

#append Añade un elemento a una lista
lista=["David","Andrés","Murguia"]
print(lista)
lista.append("Villarreal")
print(lista)

#extend Concatena listas
lista2=["David","Andrés"]
print(lista2)
lista2.extend(["Murguia","Villarreal"])
print(lista2)

#insert Añade elementos a una lista en una posicion especifica
lista3=[1,2,3,["David","Andrés"],5,6,7]
print(lista3)
lista3.insert(4,["Murguia","Villarreal"])
print(lista3)

#del Elimina un elemento en una posicion especifica en una lista
lista4=[6,1,2,3,4,5]
print(lista4)
del lista4[0]
print(lista4)

#remove Elimina la primera ocurrencia de un elemento especifico
lista5=["Angel","Mauricio","Daniel","Josue","David","Daniel","Daniel"]
print(lista5)
lista5.remove("Daniel")
print(lista5)

#reverse Imprime la lista al reves
lista6=[1, 2, 3, 4, 5, 6, 7]
print(lista6)
lista6.reverse()
print(lista6)

#sort Ordena la lista en orden
#reverse=True Reversa
#key=Funcion Ordena en una funcion en especifico
lista7=[1,2,3,4,5,6,7,8,9]
print(lista7)
lista7.sort(reverse=True)
print(lista7)
lista8=["A","OK","HOY","HOLA","AMIGO","OKEY","DOS","B","A"]
def funcion_length(x):
    return len(x)

lista8.sort(key=funcion_length)
print(lista8)

#sorted Ordena la lista de mayor a menor
#O con reverse=True en reversa
lista9=[2,3,1,2,43,10,29]
print(lista9)
print(sorted(lista9))
print(sorted(lista9,reverse=True))

#min Regresa el minimo
lista10=[["Hola","Amigos"],["1","2","4"]]
print(min(lista10))
lista11=[1,2,3,2,45,32,122,3,2,1,0,656,-1]
print(min(lista11))

#max Regresa el maximo
lista12=[3,2,4,5,3,1,3,5,7,5,90909]
print(max(lista12))

#index Regresa la posicion de un elemento especifico
lista13=["Hola","que","tal","como","estan","amigos"]
print(lista13.index("tal"))

#count Regresa la cantidad de veces que aparece un elemento especifico en una lista
lista14=(1,2,3,1,2,3,4,5,3,2,1,2,3,4,2,1,2,3,4,5,5,6,7,8,6,4,3,1,2)
print(lista14.count(1))

#sum Suma todos los elementos de la lista
lista15=[1,2,3,4,3,3,2,2,2,3,4,189,5,6,7,19,82,72,34,901,76,1,9,82]
print(sum(lista15))

