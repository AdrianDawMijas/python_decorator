from instituto_decorators import add_estudiantes

@add_estudiantes( estudiantes = [{"nombre": "jose", "curso": 1},
                                 {"nombre": "maria", "curso": 1},
                                  {"nombre": "paco", "curso": 2}])
class Instituto:
    
    def __init__(self, nombre) -> None:
        self.nombre = nombre

def main():
    instituto = Instituto("IES Vega de Mijas")

    for curso, clase in instituto.clases.items():
        print(f"clase {curso}:")
        for estudiante in clase.estudiantes:
            print(estudiante)



# The following block ensures that main() is called only when the script
# is run directly, not when it's imported as a module
if __name__ == "__main__":
    main()