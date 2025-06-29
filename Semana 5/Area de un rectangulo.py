# calcular el área de un rectángulo
# Utilizamos los tipos de datos float y string, y  identificadores descriptivos

def calcular_area_rectangulo(base, altura):
    # Calcula el área multiplicando la base por la altura
    return base * altura

# agregar datos
mensaje_area = "Calculo del área de un rectángulo"
print(mensaje_area)

# Entrada de datos: base y altura
base_rectangulo = float(input("Ingrese la base del rectángulo en metros: "))
altura_rectangulo = float(input("Ingrese la altura del rectángulo en metros: "))

# Cálculo del área
area_calculada = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)

# Mostrar el resultado
print(f"El área del rectángulo es {area_calculada} metros cuadrados.")
