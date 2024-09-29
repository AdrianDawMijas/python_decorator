class Estudiante:

    def __init__(self, nombre, fecha_nacimiento, curso) -> None:
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.curso = curso

    def __str__(self) -> str:
        return f"Estudiante: nombre = {self.nombre}, fecha_nacimiento = {self.fecha_nacimiento}"