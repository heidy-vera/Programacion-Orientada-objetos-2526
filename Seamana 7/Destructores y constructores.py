# Crea un programa utilizando los constructores y destructores
# Programa para canciones
class Cancion:
    def __init__(self, titulo, artista):
        # Constructor: se ejecuta al crear una nueva canción
        self.titulo = titulo
        self.artista = artista
        print(f"Canción agregada: '{self.titulo}' de {self.artista}")

    def reproducir(self):
        # Método para simular la reproducción de la canción
        print(f" Reproduciendo: '{self.titulo}' - {self.artista}")

    def __del__(self):
        # Destructor: se ejecuta cuando el objeto se elimina
        print(f"Canción eliminada de la lista: '{self.titulo}'")

    def __del__(self):
        # Destructor: se ejecuta cuando el objeto se elimina
        print(f"Canción eliminada de la lista: '{self.titulo}'")

# Crear una canción
cancion1 = Cancion("May Way", "Calvin Harris")
cancion1.reproducir()
