class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad

    def mostrar_saldo(self):
        print("Saldo actual:", self.__saldo)

# Uso
cuenta = CuentaBancaria(100)
cuenta.depositar(70)
cuenta.retirar(30)
cuenta.mostrar_saldo()