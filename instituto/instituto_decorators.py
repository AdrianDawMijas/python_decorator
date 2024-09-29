from clase import Clase

def add_estudiantes(estudiantes):

    def decorator(cls):

        clases = {}

        for estudiante in estudiantes:
            
            curso = estudiante['curso']
            clase = clases.get(curso)

            if clase is None:
                clase = Clase(curso)
                clases[curso] = clase

            clase.estudiantes.append(estudiante)

        setattr(cls, "clases", clases)

        #decorador de clase debe devolver la clase
        return cls

    return decorator

    