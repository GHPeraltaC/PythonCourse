class Universidad:

    def __init__(self, razon_social, tipo, ubicacion):
        self.razon_social = razon_social
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.disponibilidad = True

    def info(self):
        print(f"La Universidad de {self.razon_social} de tipo {self.tipo}, se encuentra ubicado en: {self.ubicacion}")

    def inscripcion(self, estado):
        if estado == 1:
            print("Inscripciones Abiertas")
        else:
            print("Inscripciones Cerradas")

#instanciar Objeto
uni1 = Universidad("Las Artes", "Publico", "Centro")

#Llamado de funciones
uni1.info()
uni1.inscripcion(1)
