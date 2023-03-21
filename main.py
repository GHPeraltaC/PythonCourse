from func import *


"""
Comentario Varias Lineas
# VARIABLES

first_name = "Cristhofer"
last_name = "Peralta"

#full_name = first_name + " " + last_name;

full_name = f"Mi nombre es {first_name} {last_name}"

text = 'Mi primer texto es "Python"'

print(full_name)
print(len(full_name))
print(full_name.upper())
print(full_name.lower())
print(text)

"""

"""
#FUNCIONES
y = 5

def my_func():
    y = 2
    print(y)

def my_func2():
    y = 5

    def other():
        y = 3
        print(y)

    other()
    print(y)

#llamado de funciones
my_func()
my_func2()
print(y)
"""

"""
SCOPE: ALCANCE DE LAS VARIABLES
a = 1
b: int = 2
print(a + b)
"""

"""
#CONDICIONALES
a = 2

if a == 1:
    print("0")
else:
    print("-1")
    #pass - Omitir Else

"""

ARS = 202.91
COL = 4849.99
MEX = 18.74

name = input("Ingrese su nombre: ")
print(f"Hola {name}. Bienvenido al conversor de monedas")

print("1 - Dolares estadounidenses a pesos argentinos")
print("2 - Dolares estadounidenses a pesos colombianos")
print("3 - Dolares estadounidenses a pesos mexicanos")

opcion = int(input("Seleccione una opcion: "))

if opcion == 1:

    dolares = int(input("Cantidad de Dolares: "))
    pesos = ARS * dolares

    print(f"Tienes {pesos} pesos argentinos")

elif opcion == 2:

    dolares = int(input("Cantidad de Dolares: "))
    pesos = COL * dolares

    print(f"Tienes {pesos} pesos colombianos")

elif opcion == 3:

    dolares = int(input("Cantidad de Dolares: "))
    pesos = MEX * dolares

    print(f"Tienes {pesos} pesos mexicanos")

