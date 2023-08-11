from Clases.clases import *

# Crear personas
personas = [
    Persona("12345678", "Alexander", "Guevara"),
    Persona("98765432", "Josue", "Campos")
]

def imprimir_menu():
    print("***** MENÚ *****")
    print("1. LISTAR PRODUCTOS")
    print("2. AGREGAR PRODUCTOS")
    print("3. HACER UNA VENTA")
    print("4. SALIR")


# Función para el inicio de sesión
def inicio_sesion():
    dni_ingresado = input("Ingresa tu DNI: ")
    for persona in personas:
        if persona.dni == dni_ingresado:
            print(f"Bienvenido {persona.nombre} {persona.apellidos}")
            return True
    print("DNI no encontrado.")
    return False


# Desayuno
productos_desayuno = [
    Desayuno("Croissant", 2.50, "Continental", 10),
    Desayuno("Huevos Revueltos", 3.75, "Americano", 8),
    Desayuno("Tostadas con Aguacate", 4.50, "Saludable", 15),
    Desayuno("Panqueques", 3.25, "Clásico", 12),
    Desayuno("Omelette", 4.00, "Variado", 10)
]

# Almuerzo
productos_almuerzo = [
    Almuerzo("Pollo a la Parrilla", 8.50, "Especialidad", 20),
    Almuerzo("Pasta Carbonara", 7.25, "Italiano", 18),
    Almuerzo("Ensalada César", 6.75, "Light", 25),
    Almuerzo("Burger con Papas Fritas", 7.00, "Americano", 22),
    Almuerzo("Sushi Variado", 9.00, "Japonés", 16)
]

# Cena
productos_cena = [
    Cena("Salmón a la Plancha", 10.50, "Saludable", 15),
    Cena("Filete Mignon", 12.75, "Gourmet", 10),
    Cena("Pizza Margherita", 8.25, "Italiano", 18),
    Cena("Tacos de Pescado", 9.00, "Mexicano", 20),
    Cena("Sopa de Tomate", 6.50, "Clásico", 15)
]

def listar_productos():
    print("***** LISTA DE PRODUCTOS *****")
    print("\n{:<40} | {:<15} | {:<10}".format("Nombre", "Precio", "Cantidad"))
    print("=" * 75)
    
    # Lista de productos de desayuno
    print("\nDesayuno:")
    for producto in productos_desayuno:
        print("{:<40} | ${:<15.2f} | {:<10}".format(producto.nombre, producto.precio, producto.cantidad))
    
    # Lista de productos de almuerzo
    print("\nAlmuerzo:")
    for producto in productos_almuerzo:
        print("{:<40} | ${:<15.2f} | {:<10}".format(producto.nombre, producto.precio, producto.cantidad))
    
    # Lista de productos de cena
    print("\nCena:")
    for producto in productos_cena:
        print("{:<40} | ${:<15.2f} | {:<10}".format(producto.nombre, producto.precio, producto.cantidad))

# Función para agregar productos
def agregar_productos():
    nombre_producto = input("Ingresa el nombre del producto: ")
    
    # Buscar si el producto ya existe
    producto_existente = None
    for producto in productos_desayuno + productos_almuerzo + productos_cena:
        if producto.nombre == nombre_producto:
            producto_existente = producto
            break
    
    if producto_existente:
        respuesta = input(f"El producto '{nombre_producto}' ya existe. ¿Desea agregar más cantidad? (S/N): ")
        if respuesta.lower() == "s":
            cantidad_producto = int(input(f"Ingresa la cantidad adicional del producto '{nombre_producto}': "))
            producto_existente.cantidad += cantidad_producto
            print(f"Se agregó {cantidad_producto} unidades más a '{nombre_producto}'.")
        else:
            print(f"El producto '{nombre_producto}' ya existe.")
    else:
        precio_producto = float(input("Ingresa el precio del producto: "))
        cantidad_producto = int(input("Ingresa la cantidad del producto: "))
        
        tipo_producto = input("Ingresa el tipo de producto (Desayuno/Almuerzo/Cena): ")
        nuevo_producto = Producto(nombre_producto, precio_producto, cantidad_producto)
        
        if tipo_producto.lower() == "desayuno":
            productos_desayuno.append(nuevo_producto)
        elif tipo_producto.lower() == "almuerzo":
            productos_almuerzo.append(nuevo_producto)   
        elif tipo_producto.lower() == "cena":
            productos_cena.append(nuevo_producto)
        else:
            print("Tipo de producto no válido.")

# Función para hacer una venta
def hacer_venta():
    nombre_producto = input("Ingresa el nombre del producto que deseas vender: ")
    
    # Buscar si el producto existe
    producto_existente = None
    for producto in productos_desayuno + productos_almuerzo + productos_cena:
        if producto.nombre == nombre_producto:
            producto_existente = producto
            break
    
    if producto_existente:
        cantidad_deseada = int(input(f"Ingrese la cantidad de '{nombre_producto}' que deseas vender: "))
        
        if cantidad_deseada <= producto_existente.cantidad:
            producto_existente.cantidad -= cantidad_deseada
            print(f"Venta realizada: '{nombre_producto}' x{cantidad_deseada}")
        else:
            print("No hay suficiente cantidad disponible para la venta.")
    else:
        print(f"El producto '{nombre_producto}' no existe.")

# Inicio de sesión
while not inicio_sesion():
    pass  # Repetir hasta que el inicio de sesión sea exitoso

# Menú
while True:
    imprimir_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        listar_productos()
    elif opcion == "2":
        agregar_productos()
    elif opcion == "3":
        hacer_venta()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
