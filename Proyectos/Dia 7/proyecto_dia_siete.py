class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_de_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_de_cuenta = numero_de_cuenta
        self.balance = balance

    def __str__(self):
        return f"""
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Numulo de cuenta: {self.numero_de_cuenta}
        Balance: ${self.balance}"""

    def depositar(self):
        dinero_a_depositar = float(input("Ingrese cantidad de dinero a depositar: "))
        self.balance = self.balance + dinero_a_depositar
        print(f"Se depositó la cantidad de: ${dinero_a_depositar}, su saldo actual es de: ${self.balance}")

    def retirar(self):
        dinero_a_retirar = float(input("Ingrese cantidad de dinero a retirar: "))
        if dinero_a_retirar > self.balance:
            print(f"No es posible retirar la cantidad de: ${dinero_a_retirar}, su saldo es de: ${self.balance}")
        else:
            self.balance = self.balance - dinero_a_retirar
            print(f"Se retiró la cantidad de: ${dinero_a_retirar}, su saldo actual es de: ${self.balance}")

def crear_cliente():
    print("Ingrese los datos del cliente: \n")
    nombre = input("Nombre: \n")
    apellido = input("Apellido: \n")
    numero_cliente = int(input("Numero de cuenta: \n"))
    balance_cliente = float(input("Saldo: \n"))
    mi_cliente = Cliente(nombre,apellido,numero_cliente,balance_cliente)
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
            nombre_cuenta = input("Ingrese el nombre asociado de la cuenta: \n")
            clave = int(input("Ingrese su numero de cuenta para realizar la operación: \n"))
            if clave == cliente_creado.numero_de_cuenta and nombre_cuenta == cliente_creado.nombre:
                cliente_creado.depositar()
            else:
                print(f"No es posible realizar la operación, su numero de cuenta o el nombre de la cuenta no coinciden")
        elif opcion == 2:
            nombre_cuenta = input("Ingrese el nombre asociado de la cuenta: \n")
            clave = int(input("Ingrese su numero de cuenta para realizar la operación: \n"))
            if clave == cliente_creado.numero_de_cuenta and nombre_cuenta == cliente_creado.nombre:
                cliente_creado.retirar()
            else:
                print(f"No es posible realizar la operación, su numero de cuenta o el nombre de la cuenta no coinciden")
        elif opcion == 0:
            print(f"Hasta luego, {cliente_creado.nombre} , saldré")
        else:
            print("Opción invalida")

inicio()


