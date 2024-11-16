class Escuela:
    def __init__(datos):
        datos["Alumnos"] = []

    def agregar_alumno(datos):
        alumno = {
            "Nombre": input("Ingrese el nombre del alumno: "),
            "Apellido": input("Ingrese el apellido del alumno: "),
            "DNI": input("Ingrese el DNI del alumno: "),
            "Fecha de nacimiento": input("Ingrese la fecha de nacimiento del alumno: "),
            "Tutor": input("Ingrese el nombre y apellido del tutor: "),
            "Notas": [],
            "Faltas": 0,
            "Amonestaciones": 0
        }
        datos["Alumnos"].append(alumno)
        print("Alumno agregado con éxito.")

    def mostrar_datos_alumno(datos):
        if not datos["Alumnos"]:
            print("No hay alumnos registrados.")
            return
        for i, alumno in enumerate(datos["Alumnos"]):
            print(f"Alumno {i+1}:")
            print(f"Nombre: {alumno['Nombre']}")
            print(f"Apellido: {alumno['Apellido']}")
            print(f"DNI: {alumno['DNI']}")
            print(f"Fecha de nacimiento: {alumno['Fecha de nacimiento']}")
            print(f"Tutor: {alumno['Tutor']}")
            print(f"Notas: {alumno['Notas']}")
            print(f"Faltas: {alumno['Faltas']}")
            print(f"Amonestaciones: {alumno['Amonestaciones']}")
            print("------------------------")

    def modificar_datos_alumno(datos):
        if not datos["Alumnos"]:
            print("No hay alumnos registrados.")
            return
        for i, alumno in enumerate(datos["Alumnos"]):
            print(f"{i+1}. {alumno['Nombre']} {alumno['Apellido']}")
        opcion = int(input("Ingrese el número del alumno que desea modificar: ")) - 1
        if opcion < 0 or opcion >= len(datos["Alumnos"]):
            print("Opción inválida.")
            return
        alumno = datos["Alumnos"][opcion]
        print("Ingrese los nuevos datos (deje en blanco para no modificar):")
        alumno["Nombre"] = input(f"Nombre ({alumno['Nombre']}): ") or alumno["Nombre"]
        alumno["Apellido"] = input(f"Apellido ({alumno['Apellido']}): ") or alumno["Apellido"]
        alumno["DNI"] = input(f"DNI ({alumno['DNI']}): ") or alumno["DNI"]
        alumno["Fecha de nacimiento"] = input(f"Fecha de nacimiento ({alumno['Fecha de nacimiento']}): ") or alumno["Fecha de nacimiento"]
        alumno["Tutor"] = input(f"Tutor ({alumno['Tutor']}): ") or alumno["Tutor"]
        print("Datos modificados con éxito.")


