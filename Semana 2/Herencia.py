# Clase base (abstracta)
class Animal:
    def hacer_sonido(self):
        pass  # Método abstracto

# Clases hijas (heredan de Animal)
class Perro(Animal):
    def hacer_sonido(self):
        print("El perro dice: ¡Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("El gato dice: ¡Miau!")

# Uso
mi_perro = Perro()
mi_gato = Gato()

mi_perro.hacer_sonido()
mi_gato.hacer_sonido()