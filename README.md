# Proyecto 2 escuela de programacion LA CASA DEL FUTURO
# Mis Contactos

# Importación de las librerías necesarias
import flet as ft  # Importa la biblioteca flet y la renombra como ft
import winsound  # Importa la biblioteca winsound para controlar el sonido en Windows
import json  # Importa la biblioteca json para trabajar con archivos JSON

# Nombre del archivo JSON donde se guardarán los contactos
archivo_contactos = "contactos.json"

# Función para cargar los contactos desde el archivo JSON
def cargar_contactos():
    try:
        with open(archivo_contactos, "r") as archivo:
            contactos = json.load(archivo)  # Carga el contenido del archivo JSON en la variable contactos
    except FileNotFoundError:
        contactos = []  # Si el archivo no existe, crea una lista vacía de contactos
    return contactos

# Función para guardar los contactos en el archivo JSON
def guardar_contactos(contactos):
    with open(archivo_contactos, "w") as archivo:
        json.dump(contactos, archivo)  # Guarda los contactos en el archivo JSON

# Función para eliminar el último contacto de la lista
def eliminar_ultimo_contacto(contactos):
    if contactos:
        contactos.pop()  # Elimina el último elemento de la lista de contactos
        return True
    else:
        return False

# Función para mostrar todos los contactos al usuario
def mostrar_contactos(contactos):
    if not contactos:
        return "La lista de contactos está vacía."  # Retorna un mensaje si la lista de contactos está vacía
    else:
        mensaje = "Lista de Contactos:\n"
        for contacto in contactos:
            mensaje += f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correo electrónico: {contacto['email']}\n"
        return mensaje.strip()  # Elimina los espacios en blanco al principio y al final del mensaje

# Creamos la pestaña principal
def main(page):
    page.title = "Mis Contactos"  # Establece el título de la página como "Mis Contactos"
    
    class Contactos:
        def __init__(self):
            self.contactos = cargar_contactos()  # Carga los contactos al iniciar la aplicación
            self.nombre_field = ft.TextField(label="Nombre", autofocus=True)  # Campo de texto para el nombre del contacto con enfoque automático
            self.telefono_field = ft.TextField(label="Teléfono")  # Campo de texto para el número de teléfono del contacto
            self.email_field = ft.TextField(label="Correo electrónico")  # Campo de texto para el correo electrónico del contacto

        def cargar(self):
            nombre = self.nombre_field.value  # Obtiene el valor del campo de texto del nombre
            telefono = self.telefono_field.value  # Obtiene el valor del campo de texto del teléfono
            email = self.email_field.value  # Obtiene el valor del campo de texto del correo electrónico
            self.contactos.append({"nombre": nombre, "telefono": telefono, "email": email})  # Agrega un nuevo contacto a la lista de contactos
            guardar_contactos(self.contactos)  # Guarda la lista de contactos actualizada en el archivo JSON

        def eliminar_ultimo(self):
            if eliminar_ultimo_contacto(self.contactos):
                guardar_contactos(self.contactos)
                return "Último contacto eliminado de la lista."  # Retorna un mensaje si se elimina el último contacto de la lista
            else:
                return "La lista de contactos está vacía."  # Retorna un mensaje si la lista de contactos está vacía

    greetings = ft.Column()  # Columna para mostrar mensajes al usuario

    def cargar_click(e):
        contactos.cargar()  # Llama al método cargar del objeto Contactos cuando se hace clic en el botón "Cargar"
        greetings.controls.append(ft.Text("Contacto agregado a la lista."))  # Añade un mensaje de confirmación al usuario
        contactos.nombre_field.value = ""  # Reinicia el valor del campo de texto del nombre
        contactos.telefono_field.value = ""  # Reinicia el valor del campo de texto del teléfono
        contactos.email_field.value = ""  # Reinicia el valor del campo de texto del correo electrónico
        page.update()  # Actualiza la página
        contactos.nombre_field.focus()  # Establece el enfoque en el campo de texto del nombre

    def eliminar_click(e):
        mensaje = contactos.eliminar_ultimo()  # Llama al método eliminar_ultimo del objeto Contactos cuando se hace clic en el botón "Eliminar Último Contacto"
        greetings.controls.append(ft.Text(mensaje))  # Añade un mensaje al usuario según el resultado de la operación
        page.update()  # Actualiza la página

    def mostrar_click(e):
        mensaje = mostrar_contactos(contactos.contactos)  # Llama a la función mostrar_contactos cuando se hace clic en el botón "Mostrar Contactos"
        greetings.controls.append(ft.Text(mensaje))  # Añade un mensaje al usuario con la lista completa de contactos
        page.update()  # Actualiza la página

    contactos = Contactos()  # Crea una instancia de la clase Contactos
    page.add(
        contactos.nombre_field,
        contactos.telefono_field,
        contactos.email_field,
        ft.ElevatedButton("Agregar Contacto", on_click=cargar_click),  # Botón para agregar un nuevo contacto
        ft.ElevatedButton("Eliminar Último Contacto", on_click=eliminar_click),  # Botón para eliminar el último contacto agregado
        ft.ElevatedButton("Mostrar Contactos", on_click=mostrar_click),  # Botón para mostrar todos los contactos
        greetings,
    )

ft.app(target=main)  # Ejecuta la aplicación con la función principal main como objetivo
