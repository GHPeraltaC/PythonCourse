

name = input("Ingrese su nombre: ")
print(f"Hola {name}. Bienvenido al conversor de monedas")

print("1 - Dolares estadounidenses a pesos argentinos")
print("2 - Dolares estadounidenses a pesos colombianos")
print("3 - Dolares estadounidenses a pesos mexicanos")

opcion = input("Seleccione una opcion: ")

#Funcion que valida el tipo de moneda
def conversor_monedas(opcion):
    if opcion == "1":
        ARS = 202.91
        operacion_conversor(ARS, "argentinos")

    elif opcion == "2":
        COL = 4849.99
        operacion_conversor(COL, "colombianos")

    elif opcion == "3":
        MEX = 18.74
        operacion_conversor(MEX, "mexicanos")

    else:
        print("Opcion Invalida")


#Funcion que realiza operacion de conversion de la moneda
def operacion_conversor(moneda, nombre_moneda):
    dolares = int(input("Cantidad de Dolares: "))
    pesos = moneda * dolares

    print(f"Tienes {pesos} pesos {nombre_moneda}")


#Llama funcion principal
conversor_monedas(opcion)