import os

# Muestra el código fuente de un archivo .py
def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("❌ El archivo no se encontró.")
    except Exception as e:
        print(f" Error al leer el archivo: {e}")

# Menú principal
def mostrar_menu():
    ruta_base = os.path.dirname(os.path.abspath(__file__))

    # Diccionario con múltiples archivos por semana
    opciones = {
        '1': 'Semana 2/Astraccion.py',
        '2': 'Semana 3/Orientada a Objetos.py',
        '3': 'Semana 3/Tradicional.py',
        '4': 'Semana 4/EjemploMundoReal_POO.py',
        '5': 'Semana 5/Area de un rectangulo.py',
        '6': 'Semana 5/Notas de un curso.py',
        '7': 'Semana 6/Aplicacion de conocimientos.py',
        '8': 'Semana 7/Destructores y constructores.py'
    }

    while True:
        print("\n=== MENÚ PRINCIPAL - DASHBOARD ===")
        for key in sorted(opciones):
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un número para ver su código o '0' para salir: ").strip()
        if eleccion == '0':
            print("Saliendo del dashboard.")
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print(" Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    mostrar_menu()

