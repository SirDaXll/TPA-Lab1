class Asistencia:
    def __init__(self):
        self.estudiantesPresentes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantesPresentes.append(estudiante)

    def quitar_estudiante(self, estudiante):
        if estudiante in self.estudiantesPresentes:
            self.estudiantesPresentes.remove(estudiante)

    def listar_estudiantes(self):
        for estudiante in self.estudiantesPresentes:
            print(estudiante)