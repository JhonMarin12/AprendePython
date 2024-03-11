###############
### TUPLAS ####
###############

# Definicion: SImilar a la lista, diferencia esencial las listas son mutables mientras las
# Tuplas no lo son.

empty_tuple = ()
tenerife_geoloc = (28.46824, -16.251234)
three_wise_men = ("Melchor", "Gaspar", "Baltasar")

one_item_tuple = ('Jhon Marin')
# Notese que da un resultado de tipo str, para corregir esto
print(type(one_item_tuple))
one_item_tuple = ('Jhon Marin',)
print(type(one_item_tuple))

king1, king2, king3 = three_wise_men
print(king1, king3, king3)


# Desempaquetado Extendido con el operador *
ranking = ('G', 'A', 'R', 'Y', 'W')

head, *body, tail = ranking
print(head, body, tail)

# Tuplas vs Listas
# 1. Las tuplas ocupan menos espacioo en memoria
# 2. en las tuplas existen proteccion frente a cambios indeseados
# 3. Las tuplas pueden usar como clvaes de diccionarios (hashsables)
# 4. Las namedtuples son una alternativa sencilla a los objetos
