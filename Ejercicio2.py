
class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    @property
    def getTitular(self):
        return self.titular

    @property
    def getCantidad(self):
        return self.cantidad
    
    def setTitular(self):
        self.titular= input("Ingrese el Titular de la cuenta: ")
        while (self.titular.isalpha() != True) or (len(self.titular) < 3) or (self.titular== " "):
            #PROBLEMA no me admite poner el nombre completo (Nombre y Apellido) debido a la espacio entre estos.
            self.titular= input("ingrese un nombre valido")

    def setCantidad(self):
        cantidad= input("ingrese la cantidad de la cuenta: ")
        while (cantidad.isdigit()!= True) or (int(cantidad) < 0) or (cantidad.isspace()) or (cantidad== " "):
            cantidad= input("ingrese una cantidad valida ")
        self.cantidad= int(cantidad)

    def mostrar(self):
        return(f'Esta cuenta es de {self.getTitular} y tiene un saldo de ${self.getCantidad}')

    def deposito(self):
        deposito= input("ingrese la cantidad a depositar: ")
        #problema al ingresar numero entre "" me tira error y en el setCantidad() de arriba no. No he logrado encontrar el fallo o la causa.
        while (deposito== "") or (deposito.isspace()) or (int(deposito) < 0) or (deposito.isdigit() != True):
            deposito= input("Ingreso no valido, ingrese la cantidad de nuevo ")
        cantidad= int(deposito)
        self.cantidad = self.cantidad + cantidad

    def retirar(self):
        retiro= input("Ingrese el monto a retirar: ")
        while (int(retiro) > self.cantidad) or (int(retiro) < 0) or (retiro.isdigit() != True) or (retiro.isspace()) or (retiro== " "):
            print("La cantidad que desea retirar es excesiva. De otro modo el numero ingresado no es valido. ")
            retiro = input("ingrese la cantidad de nuevo: ")
        cantidad= int(retiro)
        self.cantidad = self.cantidad - cantidad

a= Cuenta("titular","cantidad")
a.setTitular()
a.setCantidad()
print("="*45)
a.deposito()
print(a.mostrar())
print("="*45)
a.retirar()
print(a.mostrar())