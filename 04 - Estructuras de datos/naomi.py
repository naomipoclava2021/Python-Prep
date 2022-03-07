## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla


lista = ['Buenos Aires', 'Brasilia', 'Asuncion', 'Montevideo', 'Santiago', 'Lima', 'Caracas', 'Bogota']
print(lista)
# 2) Imprimir por pantalla el segundo elemento de la lista
print(lista[1])

# 3) Imprimir por pantalla del segundo al cuarto elemento
print(lista[1:4])

# 4) Visualizar el tipo de dato de la lista
print(type(lista))

# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
print(lista[2:])

# 6) Visualizar los primeros 4 elementos de la lista
print(lista[:4])

# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
lista.append('Cuidad de Mexico')
lista.append('Montevideo')
print(lista)

# 8) Agregar otra ciudad, pero en la cuarta posición
lista.insert(3,'Quito')
print(lista)

# 9) Concatenar otra lista a la ya creada
lista.extend(['Madrid','Roma', 'Bruselas'])
print(lista)

# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
print(lista.index('Montevideo'))

# 11) ¿Qué pasa si se busca un elemento que no existe?
print('Florida' in lista)
print('Madrid' in lista)

# 12) Eliminar un elemento de la lista
lista.remove('Lima')
print(lista)

# 13) ¿Qué pasa si el elemento a eliminar no existe?


# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
eliminado = lista.pop()
print(eliminado)

# 15) Mostrar la lista multiplicada por 4
lista_repetido = lista *4
print(lista_repetido)
lista_repetido.sort()
print(lista_repetido)


# 16) Crear una tupla que contenga los números enteros del 1 al 20
# tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
#for i in range(30,100):
#    print(i)
tupla = (tuple(range(1,21)))
print(tupla)


# 17) Imprimir desde el índice 10 al 15 de la tupla
print(tupla[10:16])

# 18) Evaluar si los números 20 y 30 están dentro de la tupla
print(20 in tupla)
print(30 in tupla)

# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
elemento = 'Paris'
if (not(elemento in lista)):
    lista.append(elemento)
    print(elemento, 'se agrego a la lista')
else:
    print(elemento, 'ya existia')

print(lista)

# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
print(lista_repetido)
print(lista_repetido.count('Caracas'))

print(tupla.count(12))

# 21) Convertir la tupla en una lista
print(list(tupla))

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
v1,v2,v3 = tupla[:3]
print(v1)
print(v2)
print(v3)

# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
diccionario = {
    "ciudad":lista,
    "Pais": ['Argentina', 'Italia'],
    "Continente": ['Europea', 'Oriental']
}
print(diccionario)
# 24) Imprimir las claves del diccionario
print(diccionario.keys())
# 25) Imprimir las ciudades a través de su clave
print(diccionario['ciudad'])

