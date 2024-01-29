class Persona():

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self,nombre, apellido,numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_de_cuenta = numero_cuenta
        self.balance = balance

    def imprimir_informacion(self,nombre,apellido,numero_cuenta,balance):
        print(f"Cliente: {nombre} {apellido}\nNúmero de cuenta: {numero_cuenta}\nBalance: {balance}")

    def depositar(self,nombre,apellido,numero_cuenta,balance):
        cuenta = int(input("Ingrese su número de cuenta:\n"))
        if cuenta == numero_cuenta:
            cantidad_a_depositar = int(input("¿Cuánto dinero desea depositar a su cuenta?\n"))
            print(f"El número de cuenta corresponde a {nombre} {apellido}")
            balance += cantidad_a_depositar
            print(f"Felicidades, depositó {cantidad_a_depositar}.\nSu saldo actual es de {balance}")
        else:
            print(f"El número {cuenta} no corresponde a su cuenta")

    def retirar(self,nombre,apellido,numero_cuenta,balance):

