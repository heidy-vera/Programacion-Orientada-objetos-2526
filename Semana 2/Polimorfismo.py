class Animal:
    def hacer_sonido(self):
        print("Este animal hace un sonido.")

class Perro(Animal):
    def hacer_sonido(self):
        print("¡Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("¡Miau!")

class Pájaro(Animal):
    def hacer_sonido(self):
        print("¡Pío!")

# Función que usa polimorfismo
def escuchar_sonido(animal):
    animal.hacer_sonido()

# Lista de animales
animales = [Perro(), Gato(), Pájaro()]

# Usamos la misma función para todos
for a in animales:
    escuchar_sonido(a)