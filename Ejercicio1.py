
class Persona:
    def __init__(self, nombre, dni, edad):
        self.nombre= nombre
        self.dni = dni
        self.edad= edad

    # con property indicamos a Python que el método deberá ser tratado como un atributo. Un Atributo únicamente de lectura.
    @property
    def getNombre(self):
        return self.nombre

    @property
    def getDni(self):
        return self.dni

    @property
    def getEdad(self):
        return self.edad

    def setNombre(self):
        self.nombre = input("ingrese su Nombre: ")
        #no valida el espacio para "maria paula" y no tiene limite maximo de caracteres
        while self.nombre.isalpha() != True or len(self.nombre) <3 or self.nombre.isspace():
            self.nombre=input("ingrese un nombre valido: ")
            if not self.nombre:
                continue

    def setDni(self):
        self.dni = input("ingrese su DNI: ")
        #no valida el maximo de caracteres, tenes muchas condiciones en 1 sola instruccion, si cumple al menos 1 entra al ciclo
        while self.dni.isdigit() != True or len(self.dni) <8 or self.dni.isspace():
            self.dni= input("ingrese un dni valido: ")
            if not self.dni:
                continue


    def setEdad(self):
        edad = input("ingrese su edad: ")
        #no tiene limite maximo definido, puede colocarse 99años por ejemplo
        while edad.isdigit() != True or int(edad) <0 or edad.isspace():
            edad= input("ingrese una edad valida: ")
            if not edad: #----> para verificar si esta vacio. una variable vacia se evalua como False y si tiene contenido como True.
                continue
        self.edad= int(edad)

    def mostrar(self): #no muestra si es mayor de edad al finalizar la ejecucion siendo edad= 100 por ejemplo
        return f'la persona: {self.getNombre}  con el dni  {self.getDni} tiene {self.getEdad}'

    def mayorEdad(self):
            if self.edad >= 18:
                return "es mayor de edad"
            else:
                return "es menor"
            


a = Persona("nombre","dni","edad")
b = Persona("nombre","dni","edad")
a.setNombre()
a.setDni()
a.setEdad()
# b.setNombre()
# b.setDni()
# b.setEdad()
a.mayorEdad()
# b.mayorEdad()
#no imprime si es mayor de edad que es lo que pide el ejercicio --> print(a.mayorEdad()) puede ser una sugerencia

print(a.mostrar())
# b.mostrar()
# a.mayorEdad()
# b.mayorEdad()
