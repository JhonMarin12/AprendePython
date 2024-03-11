######################
#### Diccionarios ####
######################

#analogia con otros lenguajes de programacion (Arrays asociativos, hashes, hashmaps)

#Crear un diccionario
empty_dict = {}

rae = {
    'bifronte' : 'De dos frentes o dos caras',
    'anarcoide' : 'que tiene desorden',
    'montuvio' : 'Campesion de la costa'
}

population_can = {
    2015: 2_135_209,
    2016: 2_154_924,
    2017: 2_177_048,
    2018: 2_206_901,
    2019: 2_220_270
}

### Se puede crear un diccionario especificando sus claves y un unico valor de relleno

prueba = dict.fromkeys('aeiou',0)
#print(prueba)


### Obtener un valor de un diccionario
# print(population_can[2015])
# print(population_can.get(2017))
# print(population_can.get(2020))
# print(population_can.get(2020, 0))


### Creando desde el vacio

VOWELS = 'aeiou'

enum_vowels = {}

for i, vowel in enumerate(VOWELS, start=1):
    enum_vowels[vowel] = i

print(enum_vowels)
