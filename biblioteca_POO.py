

#POO ejercicio 2



import json
import os

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, año_publicacion, unidades):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.disponible = True
        self.unidades = unidades

    def prestar(self):
        if self.disponible and self.unidades > 0:
            self.unidades -= 1
            if self.unidades == 0:
                self.disponible = False
            return True
        return False

    def recibir(self):
        self.unidades += 1
        if self.unidades > 0:
            self.disponible = True

# Clase Biblioteca
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, titulo):
        self.libros = [libro for libro in self.libros if libro.titulo != titulo]

    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            for libro in self.libros:
                print(f"Título: {libro.titulo}, Autor: {libro.autor}, Año: {libro.año_publicacion}, Unidades: {libro.unidades}, Disponible: {libro.disponible}")

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.prestar():
                    print(f"El libro '{titulo}' ha sido prestado.")
                    return
                else:
                    print(f"No hay unidades disponibles para el libro '{titulo}'.")
                    return
        print(f"El libro '{titulo}' no se encuentra en la biblioteca.")

    def recibir_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.recibir()
                print(f"El libro '{titulo}' ha sido devuelto.")
                return
        print(f"El libro '{titulo}' no se encuentra en la biblioteca.")

    def guardar_biblioteca(self):
        datos = []
        for libro in self.libros:
            datos.append({
                "titulo": libro.titulo,
                "autor": libro.autor,
                "año_publicacion": libro.año_publicacion,
                "disponible": libro.disponible,
                "unidades": libro.unidades
            })
        with open(f'{self.nombre}.json', 'w') as archivo:
            json.dump(datos, archivo, indent=4)
        print(f"Biblioteca '{self.nombre}' guardada en archivo JSON.")

    @staticmethod
    def cargar_biblioteca(nombre):
        if not os.path.exists(f'{nombre}.json'):
            print(f"El archivo {nombre}.json no existe.")
            return Biblioteca(nombre)

        with open(f'{nombre}.json', 'r') as archivo:
            datos = json.load(archivo)

        biblioteca = Biblioteca(nombre)
        for item in datos:
            libro = Libro(item['titulo'], item['autor'], item['año_publicacion'], item['unidades'])
            libro.disponible = item['disponible']
            biblioteca.agregar_libro(libro)

        print(f"Biblioteca '{nombre}' cargada desde archivo JSON.")
        return biblioteca

# Sistema de gestión de bibliotecas
class SistemaBibliotecas:
    def __init__(self):
        self.bibliotecas = {}

    def agregar_biblioteca(self, nombre):
        if nombre in self.bibliotecas:
            print(f"La biblioteca '{nombre}' ya existe.")
        else:
            self.bibliotecas[nombre] = Biblioteca(nombre)
            print(f"Biblioteca '{nombre}' creada.")

    def eliminar_biblioteca(self, nombre):
        if nombre in self.bibliotecas:
            del self.bibliotecas[nombre]
            print(f"Biblioteca '{nombre}' eliminada.")
        else:
            print(f"La biblioteca '{nombre}' no existe.")

    def seleccionar_biblioteca(self, nombre):
        if nombre in self.bibliotecas:
            return self.bibliotecas[nombre]
        else:
            print(f"La biblioteca '{nombre}' no existe.")
            return None

# Ejemplo de uso del sistema de bibliotecas
sistema = SistemaBibliotecas()

# Crear dos bibliotecas
sistema.agregar_biblioteca("Central")
sistema.agregar_biblioteca("Secundaria")

# Seleccionar la biblioteca "Central"
biblioteca_central = sistema.seleccionar_biblioteca("Central")
if biblioteca_central:
    # Agregar libros a la biblioteca "Central"
    libro1 = Libro("Juego de Tronos", "George R. R. Martin", 1996, 5)
    libro2 = Libro("Choque de Reyes", "George R. R. Martin", 1998, 3)
    libro3 = Libro("Tormenta de Espadas", "George R. R. Martin", 2000, 4)
    libro4 = Libro("Festín de Cuervos", "George R. R. Martin", 2005, 2)
    libro5 = Libro("Danza de Dragones", "George R. R. Martin", 2011, 1)
    biblioteca_central.agregar_libro(libro1)
    biblioteca_central.agregar_libro(libro2)
    biblioteca_central.agregar_libro(libro3)
    biblioteca_central.agregar_libro(libro4)
    biblioteca_central.agregar_libro(libro5)

    # Mostrar libros disponibles
    biblioteca_central.mostrar_libros()

    # Prestar un libro
    biblioteca_central.prestar_libro("Juego de Tronos")

    # Mostrar libros disponibles nuevamente
    biblioteca_central.mostrar_libros()

    # Recibir un libro
    biblioteca_central.recibir_libro("Juego de Tronos")

    # Mostrar libros disponibles nuevamente
    biblioteca_central.mostrar_libros()

    # Guardar la biblioteca en un archivo JSON
    biblioteca_central.guardar_biblioteca()

# Cargar la biblioteca desde un archivo JSON
biblioteca_cargada = Biblioteca.cargar_biblioteca("Central")
if biblioteca_cargada:
    # Mostrar libros de la biblioteca cargada
    biblioteca_cargada.mostrar_libros()
import json
import os

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, año_publicacion, unidades):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.disponible = True
        self.unidades = unidades

    def prestar(self):
        if self.disponible and self.unidades > 0:
            self.unidades -= 1
            if self.unidades == 0:
                self.disponible = False
            return True
        return False

    def recibir(self):
        self.unidades += 1
        if self.unidades > 0:
            self.disponible = True

# Clase Biblioteca
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, titulo):
        self.libros = [libro for libro in self.libros if libro.titulo != titulo]

    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            for libro in self.libros:
                print(f"Título: {libro.titulo}, Autor: {libro.autor}, Año: {libro.año_publicacion}, Unidades: {libro.unidades}, Disponible: {libro.disponible}")

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.prestar():
                    print(f"El libro '{titulo}' ha sido prestado.")
                    return
                else:
                    print(f"No hay unidades disponibles para el libro '{titulo}'.")
                    return
        print(f"El libro '{titulo}' no se encuentra en la biblioteca.")

    def recibir_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.recibir()
                print(f"El libro '{titulo}' ha sido devuelto.")
                return
        print(f"El libro '{titulo}' no se encuentra en la biblioteca.")

    def guardar_biblioteca(self):
        datos = []
        for libro in self.libros:
            datos.append({
                "titulo": libro.titulo,
                "autor": libro.autor,
                "año_publicacion": libro.año_publicacion,
                "disponible": libro.disponible,
                "unidades": libro.unidades
            })
        with open(f'{self.nombre}_archivo_biblioteca.json', 'w') as archivo:
            json.dump(datos, archivo, indent=4)
        print(f"Biblioteca '{self.nombre}' guardada en archivo JSON.")

    @staticmethod
    def cargar_biblioteca(nombre):
        archivo_nombre = f'{nombre}_archivo_biblioteca.json'
        if not os.path.exists(archivo_nombre):
            print(f"El archivo {archivo_nombre} no existe.")
            return Biblioteca(nombre)

        with open(archivo_nombre, 'r') as archivo:
            datos = json.load(archivo)

        biblioteca = Biblioteca(nombre)
        for item in datos:
            libro = Libro(item['titulo'], item['autor'], item['año_publicacion'], item['unidades'])
            libro.disponible = item['disponible']
            biblioteca.agregar_libro(libro)

        print(f"Biblioteca '{nombre}' cargada desde archivo JSON.")
        return biblioteca

# Sistema de gestión de bibliotecas
class SistemaBibliotecas:
    def __init__(self):
        self.bibliotecas = {}

    def agregar_biblioteca(self, nombre):
        if nombre in self.bibliotecas:
            print(f"La biblioteca '{nombre}' ya existe.")
        else:
            self.bibliotecas[nombre] = Biblioteca(nombre)
            print(f"Biblioteca '{nombre}' creada.")

    def eliminar_biblioteca(self, nombre):
        if nombre in self.bibliotecas:
            del self.bibliotecas[nombre]
            print(f"Biblioteca '{nombre}' eliminada.")
        else:
            print(f"La biblioteca '{nombre}' no existe.")

    def seleccionar_biblioteca(self, nombre):
        if nombre in self.bibliotecas:
            return self.bibliotecas[nombre]
        else:
            print(f"La biblioteca '{nombre}' no existe.")
            return None

# Ejemplo de uso del sistema de bibliotecas
sistema = SistemaBibliotecas()

# Crear dos bibliotecas
sistema.agregar_biblioteca("Central")
sistema.agregar_biblioteca("Secundaria")

# Seleccionar la biblioteca "Central"
biblioteca_central = sistema.seleccionar_biblioteca("Central")
if biblioteca_central:
    # Agregar libros a la biblioteca "Central"
    libro1 = Libro("Juego de Tronos", "George R. R. Martin", 1996, 5)
    libro2 = Libro("Choque de Reyes", "George R. R. Martin", 1998, 3)
    libro3 = Libro("Tormenta de Espadas", "George R. R. Martin", 2000, 4)
    libro4 = Libro("Festín de Cuervos", "George R. R. Martin", 2005, 2)
    libro5 = Libro("Danza de Dragones", "George R. R. Martin", 2011, 1)
    biblioteca_central.agregar_libro(libro1)
    biblioteca_central.agregar_libro(libro2)
    biblioteca_central.agregar_libro(libro3)
    biblioteca_central.agregar_libro(libro4)
    biblioteca_central.agregar_libro(libro5)

    # Mostrar libros disponibles
    biblioteca_central.mostrar_libros()

    # Prestar un libro
    biblioteca_central.prestar_libro("Juego de Tronos")

    # Mostrar libros disponibles nuevamente
    biblioteca_central.mostrar_libros()

    # Recibir un libro
    biblioteca_central.recibir_libro("Juego de Tronos")

    # Mostrar libros disponibles nuevamente
    biblioteca_central.mostrar_libros()

    # Guardar la biblioteca en un archivo JSON
    biblioteca_central.guardar_biblioteca()

# Cargar la biblioteca desde un archivo JSON
biblioteca_cargada = Biblioteca.cargar_biblioteca("Central")
if biblioteca_cargada:
    # Mostrar libros de la biblioteca cargada
    biblioteca_cargada.mostrar_libros()
