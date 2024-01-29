class Persona():

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self,nombre, apellido,numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_de_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"""
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Numulo de cuenta: {self.numero_de_cuenta}
        Balance: ${self.balance}"""

    def depositar(self):
        cuenta = int(input("Ingrese su número de cuenta:\n"))
        nombre = input("Ingrese el nombre asociado a la cuenta:\n")
        apellido = input("Ingrese el apellido asociado a la cuenta:\n")
        if (cuenta == self.numero_de_cuenta) and (nombre == self.nombre) and (apellido ==self.apellido):
            print(f"El número de cuenta corresponde a {self.nombre} {self.apellido}")
            cantidad_a_depositar = int(input("¿Cuánto dinero desea depositar a su cuenta?\n"))
            self.balance += cantidad_a_depositar
            print(f"Felicidades, depositó ${cantidad_a_depositar}.0\nSu saldo actual es de ${self.balance}")
        else:
            print(f"El número {cuenta} o el nombre {nombre+' '+apellido} no corresponde a una cuenta válida")

    def retirar(self):
        cuenta = int(input("Ingrese su número de cuenta:\n"))
        nombre = input("Ingrese el nombre asociado a la cuenta:\n")
        apellido = input("Ingrese el apellido asociado a la cuenta:\n")
        if (cuenta == self.numero_de_cuenta) and (nombre == self.nombre) and (apellido ==self.apellido):
            print(f"El número de cuenta corresponde a {self.nombre} {self.apellido}.\nEl balance actual es de {self.balance}")
            cantidad_a_retirar = int(input("¿Cuánto dinero desea retirar de su cuenta?\n"))
            while cantidad_a_retirar > self.balance:
                print(f"El valor ingresado a retirar es mayor al balance que se tiene.\nIngresa una cantidad menor o igual a ${self.balance}")
                cantidad_a_retirar = int(input("¿Cuánto dinero desea retirar de su cuenta?\n"))
            else:
                self.balance -= cantidad_a_retirar
                print(f"Retiró ${cantidad_a_retirar}.00\nEl balance actual es de ${self.balance}")
        else:
            print(f"El número {cuenta} o el nombre {nombre+' '+apellido} no corresponde a una cuenta válida")


def crear_cliente():
    print("Ingrese los datos del cliente: \n")
    nombre = input("Nombre: \n")
    apellido = input("Apellido: \n")
    numero_cuenta = int(input("Numero de cuenta: \n"))
    balance_cliente = float(input("Saldo: \n"))
    mi_cliente = Cliente(nombre,apellido,numero_cuenta,balance_cliente)
    print(f"Cliente creado")
    return mi_cliente

def inicio():
    opcion = 1
    print("Hola, vamos a crear una cuenta de banco, por favor, siguue las instrucciones: \n")
    cliente_creado = crear_cliente()
    print(cliente_creado)
    while opcion != 0:
        print("********************* MENU *********************")
        opcion = int(input("1. Depositar \n2. Retirar \n0. Salir\n"))
        if opcion == 1:
            cliente_creado.depositar()
        elif opcion == 2:
           cliente_creado.retirar()
        elif opcion == 0:
            print(f"Hasta luego, {cliente_creado.nombre} , saldré")
        else:
            print("Opción invalida")

inicio()
