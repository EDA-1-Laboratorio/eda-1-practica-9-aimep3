def agregar_producto(inventario):
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    # TODO: Crear el diccionario del producto y agregarlo a la lista
    pass

def mostrar_inventario(inventario):
    if not inventario:
        print("Inventario vacío.")
        return
    print(f"{'Nombre':<20} {'Precio':>10} {'Cantidad':>10}")
    print("-" * 42)
    # TODO: Recorrer el inventario e imprimir cada producto
    pass

def buscar_producto(inventario, nombre):
    # TODO: Buscar y retornar el producto cuyo nombre coincida
    # Retornar None si no se encuentra
    pass

def actualizar_cantidad(inventario):
    nombre = input("Nombre del producto: ")
    producto = buscar_producto(inventario, nombre)
    if producto:
        nueva_cantidad = int(input("Nueva cantidad: "))
        # TODO: Actualizar la cantidad del producto
        pass
    else:
        print("Producto no encontrado.")

def eliminar_producto(inventario):
    nombre = input("Nombre del producto a eliminar: ")
    # TODO: Buscar el producto y eliminarlo de la lista
    # Pista: usa inventario.remove(producto)
    pass

def resumen(inventario):
    if not inventario:
        print("Inventario vacío.")
        return
    # TODO: Calcular e imprimir:
    # - Total de productos distintos
    # - Valor total (sum de precio * cantidad)
    # - Producto más caro y más barato
    pass

def menu():
    inventario = []
    while True:
        print("\n=== GESTOR DE INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar cantidad")
        print("5. Eliminar producto")
        print("6. Resumen")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            producto = buscar_producto(inventario, nombre)
            if producto:
                print(producto)
            else:
                print("No encontrado.")
        elif opcion == "4":
            actualizar_cantidad(inventario)
        elif opcion == "5":
            eliminar_producto(inventario)
        elif opcion == "6":
            resumen(inventario)
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

menu()
