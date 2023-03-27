class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ruedas = 4
        self.en_marcha = True

    def encender(self):
        self.en_marcha = True
        print("Encendido")

    def apagar(self):
        self.en_marcha = False
        print("Apagado")

    def acelerar(self):
        print("Acelerando")

    def frenar(self):
        print("Frenando")

    def info(self):
        print(f"Mi vehiculo: {self.marca}, modelo: {self.modelo}, ruedas: {self.ruedas}, estado: {self.en_marcha}")


class Moto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def caballito(self):
        print("Estoy haciendo caballito")

    def info(self):
        print(f"La marca de mi moto es {self.marca} y el modelo {self.modelo}")

print("Uso clases")

v1 = Vehiculo("Ford", "F150")
v1.acelerar()
v1.frenar()
v1.encender()
v1.apagar()
v1.info()

v2 = Moto("aaa", "sss")
v2.caballito()
v2.info()