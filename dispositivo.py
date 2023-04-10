from camara import Camara

class Dispositivo(Camara):
    def __init__(self, id, nombre, resolucion, marca, modelo):
        super().__init__(id, nombre, resolucion)
        self.marca = marca
        self.modelo = modelo
        
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.nombre})"