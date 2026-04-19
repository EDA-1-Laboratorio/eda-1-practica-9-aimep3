def agregar_contacto(agenda):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    
    agenda.append({
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    })
    print("Contacto agregado.")

def listar_contactos(agenda):
    if not agenda:
        print("Agenda vacía.")
        return
    
    contactos_ordenados = sorted(agenda, key=lambda c: c["nombre"].lower())
    
    print(f"{'Nombre':<20} {'Teléfono':<15} {'Email':<25}")
    print("-" * 62)
    for c in contactos_ordenados:
        print(f"{c['nombre']:<20} {c['telefono']:<15} {c['email']:<25}")

def buscar_contacto(agenda, termino):
    # Retorna una lista con todos los contactos que contengan el término en su nombre
    return [c for c in agenda if termino.lower() in c["nombre"].lower()]

def editar_contacto(agenda):
    nombre = input("Nombre del contacto a editar: ")
    resultados = buscar_contacto(agenda, nombre)
    
    if not resultados:
        print("No se encontró el contacto.")
        return
    
    # Si hay varios, seleccionamos el primero para simplificar (o el único si solo hay 1)
    contacto = resultados[0] 
    print(f"Editando a: {contacto['nombre']}")
    
    nuevo_telefono = input(f"Nuevo teléfono (presiona Enter para mantener {contacto['telefono']}): ")
    if nuevo_telefono != "":
        contacto["telefono"] = nuevo_telefono
        
    nuevo_email = input(f"Nuevo email (presiona Enter para mantener {contacto['email']}): ")
    if nuevo_email != "":
        contacto["email"] = nuevo_email
        
    print("Contacto actualizado.")

def eliminar_contacto(agenda):
    nombre = input("Nombre del contacto a eliminar: ")
    resultados = buscar_contacto(agenda, nombre)
    
    if resultados:
        agenda.remove(resultados[0])
        print(f"Contacto eliminado.")
    else:
        print("No se encontró el contacto.")

def exportar_csv(agenda):
    if not agenda:
        print("No hay contactos para exportar.")
        return
        
    print("\n--- INICIO EXPORTACIÓN CSV ---")
    print("nombre,telefono,email")
    for c in agenda:
        print(f"{c['nombre']},{c['telefono']},{c['email']}")
    print("--- FIN EXPORTACIÓN CSV ---\n")

def estadisticas(agenda):
    if not agenda:
        print("Agenda vacía.")
        return
        
    print(f"Total de contactos: {len(agenda)}")
    
    dominios = {}
    for c in agenda:
        if "@" in c["email"]:
            dominio = c["email"].split("@")[1]
            dominios[dominio] = dominios.get(dominio, 0) + 1
            
    print("Dominios más comunes:")
    for dom, count in dominios.items():
        print(f"  {dom}: {count}")

def menu():
    agenda = []
    while True:
        print("\n=== AGENDA DE CONTACTOS ===")
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Eliminar contacto")
        print("6. Exportar CSV")
        print("7. Estadísticas")
        print("8. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            listar_contactos(agenda)
        elif opcion == "3":
            termino = input("Buscar: ")
            resultados = buscar_contacto(agenda, termino)
            if resultados:
                for c in resultados:
                    print(f"  {c['nombre']} - {c['telefono']} - {c['email']}")
            else:
                print("Sin resultados.")
        elif opcion == "4":
            editar_contacto(agenda)
        elif opcion == "5":
            eliminar_contacto(agenda)
        elif opcion == "6":
            exportar_csv(agenda)
        elif opcion == "7":
            estadisticas(agenda)
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

menu()