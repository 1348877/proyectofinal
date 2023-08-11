class Persona:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_informacion(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Cantidad: {self.cantidad}"
    
class Desayuno(Producto):
    def __init__(self, nombre, precio, tipo_desayuno, cantidad):
        super().__init__(nombre, precio, cantidad)
        self.tipo_desayuno = tipo_desayuno

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Tipo de desayuno: {self.tipo_desayuno}"

class Almuerzo(Producto):
    def __init__(self, nombre, precio, tipo_almuerzo, cantidad):
        super().__init__(nombre, precio, cantidad)
        self.tipo_almuerzo = tipo_almuerzo

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Tipo de almuerzo: {self.tipo_almuerzo}"

class Cena(Producto):
    def __init__(self, nombre, precio, tipo_cena, cantidad):
        super().__init__(nombre, precio, cantidad)
        self.tipo_cena = tipo_cena

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Tipo de cena: {self.tipo_cena}"
