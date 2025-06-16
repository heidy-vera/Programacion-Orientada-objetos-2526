# Programa tradicional para calcular el promedio de temperaturas de la semana

def pedir_temperaturas():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = []
    for dia in dias:
        temp = float(input(f"Ingrese la temperatura del {dia}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(lista):
    return sum(lista) / len(lista)

# Programa principal
temperaturas = pedir_temperaturas()
promedio = calcular_promedio(temperaturas)
print(f"\nPromedio semanal: {promedio:.2f}°C")