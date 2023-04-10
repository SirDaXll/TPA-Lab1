class Camara:
    def __init__(self, id, nombre, resolucion):
        self.id = id
        self.nombre = nombre
        self.resolucion = resolucion
    
    def transmitir(self):
        print(f"Transmitiendo desde la cámara {self.nombre} ({self.resolucion})")