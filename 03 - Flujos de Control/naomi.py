## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
from ast import For
from turtle import circle


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
n= 5
#lo que hace es : 1*2*3*4*5 hasta que x sea igual a n

if(type(n)==int):
    print(f'{n} Es un numero entero');
    if(n>0):
        x=1 #cuenta las vueltas
        f=1
        while(x<=n):
            f*=x 
            x+=1
        print(f'El factorial de {n} es: {f}');
    else:
        print(f'{n} es menor que cero');
else:
    print(f'{n} No es un numero entero');

# 7) Crear un ciclo for dentro de un ciclo while
n = 0
while(n<5):
    n+=1
    for i in range(0,n):
        print(f'Ciclo For numero: {str(i)}')
        print(f'Ciclo While numero: {str(n)}')

# 8) Crear un ciclo while dentro de un ciclo for
n = 5
for i in range(1,n):
    while(n<5):
        n-=1
    print(n, 'While')
    print(i, 'For')

# 9) Imprimir los números primos existentes entre 0 y 30
tope = 30;
n = 0;
primo = True;
while(n<tope):
    for i in range(2,n):
        if(n% i == 0):
            primo = False;
    if(primo):
        print(n)
    else:
        primo= True
    n+=1

# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
tope = 30
n = 0
primo= True
while(n<tope):
    for i in range(2,n):
        if(n % i == 0):
            primo= False
            break
    if(primo):
        print(f'los nuemro primos usando break son: {n}');
    else:
        primo = True;
    n+=1
# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
sin_ciclo_break = 0
tope = 30
n = 0
primo= True
while(n<tope):
    for i in range(2,n):
        sin_ciclo_break+=1
        if(n % i == 0):
            primo= False
    if(primo):
        print(f'los nuemro primos usando break son: {n}');
    else:
        primo = True;
    n+=1
print('Cantidad de ciclo:' + str(sin_ciclo_break))


#con break
optimizacion = 0
tope = 30
n = 0
primo= True
while(n<tope):
    for i in range(2,n):
        optimizacion+=1
        if(n % i == 0):
            primo= False
            break
    if(primo):
        print(f'Primos: {n}');
    else:
        primo = True;
    n+=1
print('--Cantidad de ciclo con 30: ' + str(optimizacion))

# Continue optimizacion
optimizacion = 0
tope = 30
n = 0
primo= True
while(n<tope):
    for i in range(2,n):
        optimizacion+=1
        if(n % i == 0):
            primo= False
            continue
    if(primo):
        print(f'Numeros Primos: {n}');
    else:
        primo = True;
    n+=1
print('Cantidad de ciclo:' + str(optimizacion))

# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
optimizacion = 0
tope = 100
n = 0
primo= True
while(n<tope):
    for i in range(2,n):
        optimizacion+=1
        if(n % i == 0):
            primo= False
            break
    if(primo):
        print(f'Primos: {n}');
    else:
        primo = True;
    n+=1
print('++Cantidad de ciclo con:' + str(optimizacion))
# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
n = 99
while(n<=300):
    n+=1
    if(n % 12 !=0):
        continue
    print(f'{str(n)} es divisible por 12')
    


# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
n = 100
while(n<=300):
    if(n% 6 == 0):
        print(f'{n} Es multiplo de 6')
        break
    n+=1