class Sesion:
    def __init__(self, id, nombreAsignatura, nombreProfesor, sala, fechaClase, horaInicio, horaFin, listaCamaras):
        self.id = id
        self.nombreAsignatura = nombreAsignatura
        self.nombreProfesor = nombreProfesor
        self.sala = sala
        self.fechaClase = fechaClase
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.camaraEnUso = None
        self.listaCamaras = listaCamaras
        
    def iniciar_transmision(self):
        if self.camaraEnUso:
            self.camaraEnUso()
        else:
            print("No se ha seleccionado una cámara para transmitir.")
            
    def terminar_transmision(self):
        print("Transmisión finalizada.")
        
    def cambiar_camara(self, indiceCamara):
        if indiceCamara >= 0 and indiceCamara < len(self.listaCamaras):
            self.camaraEnUso = self.listaCamaras[indiceCamara]
            print(f"Se ha cambiado a la cámara {self.camaraEnUso}.")
        else:
            print("Índice de cámara inválido.")