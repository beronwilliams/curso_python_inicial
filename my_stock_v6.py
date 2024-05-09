

# Proyecto 2 escuela de programacion LA CASA DEL FUTURO

# My stock v3.1

# Importación de las librerías necesarias
import flet as ft
import winsound
import json

# Nombre del archivo JSON donde se guardará el inventario
archivo_inventario = "inventario.json"

# Función para cargar el inventario desde el archivo JSON
def cargar_inventario():
    try:
        with open(archivo_inventario, "r") as archivo:
            inventario = json.load(archivo)
    except FileNotFoundError:
        inventario = []
    return inventario

# Función para guardar el inventario en el archivo JSON
def guardar_inventario(inventario):
    with open(archivo_inventario, "w") as archivo:
        json.dump(inventario, archivo)

# Función para eliminar el último producto del inventario
def eliminar_ultimo_producto(inventario):
    if inventario:
        inventario.pop()
        return True
    else:
        return False

# Función para mostrar el inventario completo al usuario
def mostrar_inventario(inventario):
    if not inventario:
        return "El inventario está vacío."
    else:
        mensaje = "Inventario:\n"
        for item in inventario:
            mensaje += f"Producto: {item['producto']}, Precio: {item['precio']}\n"
        return mensaje.strip()

# Creamos la pestaña principal
def main(page):
    page.title = "My Stock"
    
    class Inventario:
        def __init__(self):
            self.inventario = cargar_inventario()
            self.precio_field = ft.TextField(label="Precio", autofocus=True)
            self.producto_field = ft.TextField(label="Producto")

        def cargar(self):
            producto = self.producto_field.value
            precio = self.precio_field.value
            self.inventario.append({"producto": producto, "precio": precio})
            guardar_inventario(self.inventario)

        def eliminar_ultimo(self):
            if eliminar_ultimo_producto(self.inventario):
                guardar_inventario(self.inventario)
                return "Último producto eliminado del inventario."
            else:
                return "El inventario está vacío."

    greetings = ft.Column()

    def cargar_click(e):
        inventario.cargar()
        greetings.controls.append(ft.Text("Producto cargado en el inventario."))
        inventario.precio_field.value = ""
        inventario.producto_field.value = ""
        page.update()
        inventario.precio_field.focus()

    def eliminar_click(e):
        mensaje = inventario.eliminar_ultimo()
        greetings.controls.append(ft.Text(mensaje))
        page.update()

    def mostrar_click(e):
        mensaje = mostrar_inventario(inventario.inventario)
        greetings.controls.append(ft.Text(mensaje))
        page.update()

    inventario = Inventario()
    page.add(
        inventario.producto_field,
        inventario.precio_field,
        ft.ElevatedButton("Cargar", on_click=cargar_click),
        ft.ElevatedButton("Eliminar Último Producto", on_click=eliminar_click),
        ft.ElevatedButton("Mostrar Inventario", on_click=mostrar_click),
        greetings,
    )

ft.app(target=main)
