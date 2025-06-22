# Clase Producto representa un producto con nombre y cantidad disponible
class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre          # Nombre del producto
        self.cantidad = cantidad      # Cantidad en producto

    def vender(self, cantidad):
        # Método para vender cierta cantidad del producto
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad  # Reducir el producto
            print(f"Vendí {cantidad} {self.nombre}(s).")
        else:
            # No hay suficiente producto
            print(f"No hay suficiente {self.nombre}.")

# Clase Tienda que maneja varios productos
class Tienda:
    def __init__(self):
        self.productos = {}

    def agregar(self, producto):
        # Agrega un producto al inventario de la tienda
        self.productos[producto.nombre] = producto

    def vender(self, nombre, cantidad):

        if nombre in self.productos:
            self.productos[nombre].vender(cantidad)
        else:
            # Producto no encontrado en inventario
            print(f"No tenemos {nombre}.")

    def mostrar(self):
        # Muestra el inventario actual con nombre y cantidad de cada producto
        print("Inventario:")
        for p in self.productos.values():
            print(f"{p.nombre}: {p.cantidad} unidades")

# Uso
tienda = Tienda()
tienda.agregar(Producto("Camiseta", 10))
tienda.agregar(Producto("Pantalón", 5))

# Mostrar inventario inicial
tienda.mostrar()
tienda.vender("Camiseta", 3)
# Mostrar inventario después de la venta
tienda.mostrar()





