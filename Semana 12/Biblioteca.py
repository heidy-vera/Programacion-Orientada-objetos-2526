# realizar un codigo para menejar una biblioteca
# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla: título y autor inmutables
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} - {self.categoria} (ISBN: {self.isbn})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario: ISBN -> Libro
        self.usuarios = {}  # Diccionario: ID -> Usuario
        self.ids_usuarios = set()  # Conjunto para IDs únicos

    # Añadir libro
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print("El libro ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.info[0]}' agregado correctamente.")

    # Quitar libro
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("El libro no existe.")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("ID de usuario ya registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado correctamente.")

    # Dar de baja usuario
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # Prestar libro
    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros:
            print("Libro no disponible.")
            return
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        libro = self.libros.pop(isbn)
        self.usuarios[id_usuario].libros_prestados.append(libro)
        print(f"Libro '{libro.info[0]}' prestado a {self.usuarios[id_usuario].nombre}.")

    # Devolver libro
    def devolver_libro(self, isbn, id_usuario):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        usuario = self.usuarios[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro
                print(f"Libro '{libro.info[0]}' devuelto.")
                return
        print("El usuario no tiene ese libro prestado.")

    # Buscar libro por título, autor o categoría
    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    # Listar libros prestados de un usuario
    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        usuario = self.usuarios[id_usuario]
        if not usuario.libros_prestados:
            print("No tiene libros prestados.")
        else:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f"- {libro}")

# Crear biblioteca
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("1984", "George", "Ficción", "123")
libro2 = Libro("El Principito", "Antonio", "Infantil", "456")

# Agregar libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuario
usuario1 = Usuario("Ana", 1)
biblioteca.registrar_usuario(usuario1)

# Prestar libro
biblioteca.prestar_libro("123", 1)

# Listar libros prestados
biblioteca.listar_libros_prestados(1)

# Devolver libro
biblioteca.devolver_libro("123", 1)
biblioteca.listar_libros_prestados(1)

# Buscar libros por categoría
resultados = biblioteca.buscar_libro("categoria", "Ficción")
for libro in resultados:
    print(f"Encontrado: {libro}")
