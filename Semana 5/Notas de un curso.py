# calcular el promedio de tres notas y determinar si el estudiante aprueba
#  se usaron tipos de datos string y float, y  la nomenclatura CamelCase

def CalcularPromedio(nota1, nota2, nota3):
    # Retorna el promedio de las tres notas
    return (nota1 + nota2 + nota3) / 3

# Mostrar mensaje de inicio
print("Notas de los estudiantes")

# Solicitar datos del estudiante
nombreEstudiante = input("Ingrese el nombre del estudiante: ")

# Solicitar tres notas y convertirlas a tipo float
notaUno = float(input("Ingrese la primera nota: "))
notaDos = float(input("Ingrese la segunda nota: "))
notaTres = float(input("Ingrese la tercera nota: "))

# Calcular el promedio
promedioFinal = CalcularPromedio(notaUno, notaDos, notaTres)

# Mostrar resultados
print(f"\nEstudiante: {nombreEstudiante}")
print(f"Promedio final: {promedioFinal:.2f}")

# Revisar si aprueba o reprueba (mínimo 7.0 para aprobar)
if promedioFinal >= 7.0:
    print("Estado: Aprobado")
else:
    print("Estado: Reprobado")