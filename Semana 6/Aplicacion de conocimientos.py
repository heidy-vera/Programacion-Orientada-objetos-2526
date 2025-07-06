# Aplicacion de la Definición de Clase, Definición de Objeto, Herencia, Encapsulación y Polimorfismo
#Programa para venta de ropa
# Definicion de clase: Producto
class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre     # Encapsulación: atributo privado nombre
        self.precio = precio

    # Método para acceder al nombre (ya que es privado)
    def get_nombre(self):
        return self.__nombre

    # Método que puede ser sobrescrito en clases hijas
    def mostrar_detalle(self):
        print(f"Producto: {self.__nombre} - Precio: ${self.precio:.2f}")

# Clase derivada: Camisa (hereda de Producto)
class Camisa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)  # Llama al constructor de Producto
        self.talla = talla

    # Sobrescribimos el método mostrar_detalle
    def mostrar_detalle(self):
        print(f"Camisa: {self.get_nombre()}, Talla: {self.talla}, Precio: ${self.precio:.2f}")

# Clase derivada: Pantalón (heredada de Producto)
class Pantalon(Producto):
    def __init__(self, nombre, precio, color):
        super().__init__(nombre, precio)  # Llama al constructor de Producto
        self.color = color

    # Sobrescribimos el método mostrar_detalle
    def mostrar_detalle(self):
        print(f"Pantalón: {self.get_nombre()}, Color: {self.color}, Precio: ${self.precio:.2f}")


# Creacion de instancias objetos reales
producto1 = Producto("Accesorio", 10.00)  # Producto general
camisa1 = Camisa("Camisa Manga Corta", 35.00, "l")  # Objeto tipo Camisa
pantalon1 = Pantalon("Pantalón Jeans", 27.00, "Morado")  # Objeto tipo Pantalón

# Usar los métodos para mostrar detalles
producto1.mostrar_detalle()
camisa1.mostrar_detalle()
pantalon1.mostrar_detalle()
