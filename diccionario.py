
#Diccionarios Python

persona = {
    "Nombre": "Cristhofer",
    "Apellido": "Peralta",
    "Edad": 22
}

print(persona)


#Decoradores
def decorador(func):
    def envoltura():
        print("Se añade a la función original")
        func()
    return envoltura

@decorador
def saludo():
    print("Hola")

saludo()