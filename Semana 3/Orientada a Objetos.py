# Programa con POO para calcular el promedio de temperaturas de la semana

class ClimaSemana:
    def __init__(self):
        self.temperaturas = []

    def ingresar_datos(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        for dia in dias:
            temp = float(input(f"Ingrese la temperatura del {dia}: "))
            self.temperaturas.append(temp)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Programa principal
semana = ClimaSemana()
semana.ingresar_datos()
print(f"\nPromedio semanal: {semana.promedio():.2f}°C")