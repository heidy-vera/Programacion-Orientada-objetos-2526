# Realizar  un programa que gestióne un inventario para una tienda, que incorpore las colecciones en POO

import os
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self): return self.id
    def get_nombre(self): return self.nombre
    def get_cantidad(self): return self.cantidad
    def get_precio(self): return self.precio

    def set_cantidad(self, cantidad):
        if cantidad >= 0: self.cantidad = cantidad
        else: print("Error: la cantidad no puede ser negativa.")

    def set_precio(self, precio):
        if precio >= 0: self.precio = precio
        else: print("Error: el precio no puede ser negativo.")

    def __str__(self):
        return f"ID: {self.id} | {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def to_line(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}\n"
    def from_line(linea):
        try:
            id_, nombre, cant, prec = linea.strip().split(",")
            return Producto(id_, nombre, int(cant), float(prec))
        except:
            return None

# Clase Inventario

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}  # Diccionario {id: Producto}
        self.cargar()

    def cargar(self):
        if not os.path.exists(self.archivo):
            open(self.archivo, "w").close()
            return
        with open(self.archivo, "r") as f:
            for linea in f:
                p = Producto.from_line(linea)
                if p: self.productos[p.get_id()] = p

    def guardar(self):
        with open(self.archivo, "w") as f:
            f.writelines(p.to_line() for p in self.productos.values())

    # Operaciones principales
    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Error: Producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            self.guardar()
            print("Producto agregado.")

    def eliminar_producto(self, id_):
        if self.productos.pop(id_, None):
            self.guardar()
            print("Producto eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_, cantidad=None, precio=None):
        p = self.productos.get(id_)
        if not p:
            print("Error: Producto no encontrado.")
            return
        if cantidad is not None: p.set_cantidad(cantidad)
        if precio is not None: p.set_precio(precio)
        self.guardar()
        print("Producto actualizado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print("Resultados de búsqueda:")
            for p in encontrados: print(p)
        else:
            print("No se encontraron productos.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            print("\nInventario de la tienda:")
            for p in self.productos.values():
                print(p)

    # Integración de colecciones

    def lista_precios(self): return [p.get_precio() for p in self.productos.values()]
    def conjunto_nombres(self): return {p.get_nombre() for p in self.productos.values()}
    def tuplas_productos(self): return [(p.get_id(), p.get_nombre(), p.get_cantidad(), p.get_precio())
                                       for p in self.productos.values()]

def menu():
    inv = Inventario()
    while True:
        print("\n--- MENÚ INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Mostrar lista de precios")
        print("7. Mostrar conjunto de nombres únicos")
        print("8. Mostrar productos en tuplas")
        print("9. Salir")

        op = input("Seleccione una opción: ")

        if op == "1":
            id_ = input("ID: ")
            nombre = input("Nombre: ")
            try:
                cant = int(input("Cantidad: "))
                prec = float(input("Precio: "))
                inv.agregar_producto(Producto(id_, nombre, cant, prec))
            except ValueError:
                print("Error: cantidad y precio deben ser numéricos.")
        elif op == "2":
            inv.eliminar_producto(input("ID del producto a eliminar: "))
        elif op == "3":
            id_ = input("ID del producto a actualizar: ")
            cant = input("Nueva cantidad (Enter = no cambiar): ")
            prec = input("Nuevo precio (Enter = no cambiar): ")
            inv.actualizar_producto(id_,
                                    int(cant) if cant else None,
                                    float(prec) if prec else None)
        elif op == "4":
            inv.buscar_producto(input("Nombre a buscar: "))
        elif op == "5":
            inv.mostrar_inventario()
        elif op == "6":
            print("Lista de precios:", inv.lista_precios())
        elif op == "7":
            print("Conjunto de nombres únicos:", inv.conjunto_nombres())
        elif op == "8":
            print("Productos en tuplas:", inv.tuplas_productos())
        elif op == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()

