## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
from ast import For


n = 12

if(n>0):
    print(n,'es mayor que cero');
elif(n<0):
    print(n, 'es menor que cero');
else:
    print(n, 'es igual a cero');

# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
a= 43
b= True

if(type(a)== type(b)):
    print(a, 'Es de clase:',type(a), ' y ', b, 'Es de clase:',type(b), 'Tienen el mismo tipo de dato');
else:
    print(a, 'Es de clase:',type(a), ' y ', b, 'Es de clase:',type(b), 'Los tipos de datos son diferentes');

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for i in range(1,21):
    if(i % 2 == 0):
        print(str(i),'Es Par');
    else:
        print(str(i), 'Es Impar');

# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

for i in range(0,6):
    print(i,'Elevado a la potencia de 3 es: ', (i**3));

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
n= 7
for i in range(0,n):
    pass
print('Este ciclo se repite',i)

# 6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# 7) Crear un ciclo for dentro de un ciclo while

# 8) Crear un ciclo while dentro de un ciclo for

# 9) Imprimir los números primos existentes entre 0 y 30

# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6