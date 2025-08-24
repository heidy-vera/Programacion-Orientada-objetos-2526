# Modificacion del codigo anterior productos de tienda
import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id_producto = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id_producto(self):
        return self._id_producto

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_id_producto(self, id_producto):
        self._id_producto = id_producto

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self._cantidad = cantidad
        else:
            print("Error: la cantidad no puede ser negativa.")

    def set_precio(self, precio):
        if precio >= 0:
            self._precio = precio
        else:
            print("Error: el precio no puede ser negativo.")

    def __str__(self):
        return f"{self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"

    # Convertir a línea de texto
    def to_line(self):
        return f"{self._id_producto},{self._nombre},{self._cantidad},{self._precio}\n"

    # Crear producto desde línea de texto
    def from_line(linea):
        try:
            id_producto, nombre, cantidad, precio = linea.strip().split(",")
            return Producto(id_producto, nombre, int(cantidad), float(precio))
        except:
            return None


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = {}
        self.archivo = archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        if not os.path.exists(self.archivo):
            # Crear archivo vacío si no existe
            try:
                open(self.archivo, "w").close()
                print("Archivo de inventario creado.")
            except PermissionError:
                print("Error: no se tienen permisos para crear el archivo.")
            return

        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    producto = Producto.from_line(linea)
                    if producto:
                        self.productos[producto.get_id_producto()] = producto
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("Error: archivo no encontrado.")
        except PermissionError:
            print("Error: no se tienen permisos para leer el archivo.")
        except Exception as e:
            print("Error al leer el archivo:", e)

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(producto.to_line())
        except PermissionError:
            print("Error: no se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print("Error al guardar el archivo:", e)

    def agregar_producto(self, producto):
        if producto.get_id_producto() in self.productos:
            print("Error: Producto ya existe.")
        else:
            self.productos[producto.get_id_producto()] = producto
            self.guardar_en_archivo()
            print("Producto agregado y guardado en archivo.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado y archivo actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            self.guardar_en_archivo()
            print("Producto actualizado y guardado en archivo.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)


def menu():
    inventario = Inventario()
    while True:
        print("\n--- MENÚ INVENTARIO ---")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '6':
            print("Saliendo del programa...")
            break
        elif opcion == '1':
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: cantidad y precio deben ser numéricos.")
        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_inventario()
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
