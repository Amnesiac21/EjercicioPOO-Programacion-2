from multiprocessing.sharedctypes import Value
from Ejercicio2 import *
#Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva
# clase CuantaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del
# titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por
# ciento.Construye los siguientes métodos para la clase:
#  Un constructor.
#  Los setters y getters para el nuevo atributo.
#  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad.,
# por lo tanto hay que crear un método esTitularValido() que devuelve verdadero
# si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
#  Además la retirada de dinero sólo se podrá hacer si el titular es válido.
#  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
# Piensa los métodos heredados de la clase madre que hay que reescribir.


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, edad,bonificacion):
        super().__init__(titular, cantidad)
        self.edad = edad
        self.bonificacion= bonificacion

    @property
    def getBonificacion(self):
        return self.bonificacion

    @property
    def getEdad(self):
        return self.edad

    def validarEdad(self):
        #aqui si use un try para validar.
        while True:
            try:
                edad= int(input("Ingrese su edad: "))
                self.setEdad(edad)
            except ValueError:
                print("escribe una edad valida")
                continue
            if (edad<=0) or (edad>99):
                print("Ingrese una edad valida.")
                continue
            else:
                break

    def setEdad(self,value):
        self.edad= value

    def calcularBonificacion(self):
        if self.esTitularValido():
            porcentaje= int(input("ingrese el porcentaje del bono: "))
            self.bonificacion = self.cantidad * (porcentaje/100)
        else:
            self.bonificacion=0

    def esTitularValido(self):
        if self.edad >= 18 and self.edad < 25:
            return True
        else:
            return False

    def mostrar(self):
        print(super().mostrar())
        return(f'\n la cuenta tiene una bonificacion de {self.getBonificacion}') 

    def retirar(self):
        if self.esTitularValido() == True:
            super().retirar()
        else: 
            return("titular no valido para retirar.")


b = CuentaJoven("nombre", "cantidad", "edad","bonificacion")
b.setTitular()
print(b.getTitular)
b.setEdad("20")
b.validarEdad()
print(b.esTitularValido())
b.setCantidad()
b.deposito()
print("="*45)
b.calcularBonificacion()
print(b.mostrar())
print("="*45)
b.retirar()
print(b.mostrar())

