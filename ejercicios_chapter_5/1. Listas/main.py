### LISTA EN PYTHON

a  = [] #Una lista vacia
a = [1,2,3] #Lista de numeros
a = ["a", "hola", "adios"] #Lista de strings
a = [1, 2, "a", "", 12.4] #Pueden tener distintos tipos de datos

### FORMAS DE REVERTIR UNA LISTA
# 1) lista[::-1]
# 2) list(reversed(lista))
# 3) lista.reverse()

#La diferencia radica es que las dos primeras crea una nueva lista mientras que la ultima modifica la lista que ya existe


### FORMAS DE ELIMINAR ELEMENTOS DE UNA LISTA

# 1) del lista[0]
# 2) lista.remove('nombre_de_lo_que_quiero_borrar')
# 3) lista.pop(-1) que ademas puede guardar el elemento que se desea borrar
# 4) lista[1:4] = [] troceado y listas vacias

### FORMAS DE BORRAR UNA LISTA

# 1) lista.clear() regresa la lista vacia
# 2) lista = []