import string

def limpiar_texto(texto):
    # Función auxiliar para quitar signos de puntuación y pasar a minúsculas
    texto_limpio = texto.lower()
    for puntuacion in string.punctuation + "¿¡":
        texto_limpio = texto_limpio.replace(puntuacion, "")
    return texto_limpio

def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def contar_oraciones(texto):
    # Contamos cuántas veces aparecen los puntos, signos de exclamación y de interrogación de cierre
    return texto.count('.') + texto.count('!') + texto.count('?')

def palabra_mas_frecuente(texto):
    texto_limpio = limpiar_texto(texto)
    palabras = texto_limpio.split()
    
    if not palabras:
        return None
        
    frecuencias = {}
    for p in palabras:
        frecuencias[p] = frecuencias.get(p, 0) + 1
        
    # Encontrar la llave con el valor máximo
    palabra_top = max(frecuencias, key=frecuencias.get)
    return palabra_top

def palabras_unicas(texto):
    texto_limpio = limpiar_texto(texto)
    # Convertimos la lista de palabras en un set (conjunto) para eliminar duplicados
    return set(texto_limpio.split())

def longitud_promedio_palabras(texto):
    texto_limpio = limpiar_texto(texto)
    palabras = texto_limpio.split()
    
    if not palabras:
        return 0
        
    total_letras = sum(len(p) for p in palabras)
    return total_letras / len(palabras)

def buscar_palabra(texto, palabra):
    texto_limpio = limpiar_texto(texto)
    palabra_limpia = limpiar_texto(palabra)
    palabras = texto_limpio.split()
    return palabras.count(palabra_limpia)

def reemplazar_palabra(texto, vieja, nueva):
    # Reemplazo básico (Nota: afecta a subcadenas también, pero cumple con el ejercicio)
    return texto.replace(vieja, nueva)

# Texto de ejemplo para analizar
texto_ejemplo = """
Python es un lenguaje de programación muy popular. Python es fácil de aprender.
Muchos programadores usan Python para ciencia de datos y para desarrollo web.
Python tiene una gran comunidad. La comunidad de Python es muy activa y amigable.
¿Te gusta programar? ¡Python es una excelente opción para empezar!
"""

print("=== ANALIZADOR DE TEXTO ===")
print(f"Total de palabras: {contar_palabras(texto_ejemplo)}")
print(f"Total de oraciones: {contar_oraciones(texto_ejemplo)}")
print(f"Palabra más frecuente: {palabra_mas_frecuente(texto_ejemplo)}")
print(f"Palabras únicas: {len(palabras_unicas(texto_ejemplo))}")
print(f"Longitud promedio: {longitud_promedio_palabras(texto_ejemplo):.1f}")
print(f"Veces que aparece 'Python': {buscar_palabra(texto_ejemplo, 'Python')}")

nuevo = reemplazar_palabra(texto_ejemplo, "Python", "Java")
print(f"\nTexto modificado (primeras 100 letras):\n{nuevo[:100]}...")