import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class Autor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_info(self):
        return f"Autor: {self.nombre} {self.apellido}"

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        return f"Categoría: {self.nombre}"

class Libro:
    def __init__(self, titulo, isbn, autor, categoria):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.categoria = categoria

    def mostrar_info(self):
        return f"Libro: {self.titulo} (ISBN: {self.isbn}), {self.autor.mostrar_info()}, {self.categoria.mostrar_info()}"

class Usuario:
    def __init__(self, nombre, apellido, id_usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.id_usuario = id_usuario

    def mostrar_info(self):
        return f"Usuario: {self.nombre} {self.apellido} (ID: {self.id_usuario})"

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion=None):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def mostrar_info(self):
        devolucion = self.fecha_devolucion if self.fecha_devolucion else "No devuelto"
        return f"Préstamo: {self.libro.titulo}, Usuario: {self.usuario.nombre} {self.usuario.apellido}, Desde: {self.fecha_prestamo}, Hasta: {devolucion}"

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def realizar_prestamo(self, libro, usuario, fecha_prestamo):
        prestamo = Prestamo(libro, usuario, fecha_prestamo)
        self.prestamos.append(prestamo)

    def devolver_libro(self, prestamo, fecha_devolucion):
        prestamo.fecha_devolucion = fecha_devolucion

    def mostrar_libros(self):
        return [libro.mostrar_info() for libro in self.libros]

    def mostrar_prestamos(self):
        return [prestamo.mostrar_info() for prestamo in self.prestamos]

    def mostrar_usuarios(self):
        return [usuario.mostrar_info() for usuario in self.usuarios]

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Biblioteca")
        self.geometry("800x600")

        self.biblioteca = Biblioteca()
        self.create_widgets()

    def create_widgets(self):
        # Frame para gestionar libros
        self.frame_libros = tk.LabelFrame(self, text="Gestión de Libros")
        self.frame_libros.pack(fill="both", expand="yes", padx=10, pady=10)

        tk.Label(self.frame_libros, text="Título:").grid(row=0, column=0, padx=5, pady=5)
        self.titulo_entry = tk.Entry(self.frame_libros)
        self.titulo_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_libros, text="ISBN:").grid(row=1, column=0, padx=5, pady=5)
        self.isbn_entry = tk.Entry(self.frame_libros)
        self.isbn_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_libros, text="Autor:").grid(row=2, column=0, padx=5, pady=5)
        self.autor_entry = tk.Entry(self.frame_libros)
        self.autor_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.frame_libros, text="Categoría:").grid(row=3, column=0, padx=5, pady=5)
        self.categoria_entry = tk.Entry(self.frame_libros)
        self.categoria_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Button(self.frame_libros, text="Registrar Libro", command=self.registrar_libro).grid(row=4, column=0, columnspan=2, pady=10)

        # Frame para gestionar usuarios
        self.frame_usuarios = tk.LabelFrame(self, text="Gestión de Usuarios")
        self.frame_usuarios.pack(fill="both", expand="yes", padx=10, pady=10)

        tk.Label(self.frame_usuarios, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.nombre_usuario_entry = tk.Entry(self.frame_usuarios)
        self.nombre_usuario_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_usuarios, text="Apellido:").grid(row=1, column=0, padx=5, pady=5)
        self.apellido_usuario_entry = tk.Entry(self.frame_usuarios)
        self.apellido_usuario_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_usuarios, text="ID Usuario:").grid(row=2, column=0, padx=5, pady=5)
        self.id_usuario_entry = tk.Entry(self.frame_usuarios)
        self.id_usuario_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self.frame_usuarios, text="Registrar Usuario", command=self.registrar_usuario).grid(row=3, column=0, columnspan=2, pady=10)

        # Frame para gestionar préstamos
        self.frame_prestamos = tk.LabelFrame(self, text="Gestión de Préstamos")
        self.frame_prestamos.pack(fill="both", expand="yes", padx=10, pady=10)

        tk.Label(self.frame_prestamos, text="Título del Libro:").grid(row=0, column=0, padx=5, pady=5)
        self.titulo_prestamo_entry = tk.Entry(self.frame_prestamos)
        self.titulo_prestamo_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_prestamos, text="ID Usuario:").grid(row=1, column=0, padx=5, pady=5)
        self.id_usuario_prestamo_entry = tk.Entry(self.frame_prestamos)
        self.id_usuario_prestamo_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.frame_prestamos, text="Realizar Préstamo", command=self.realizar_prestamo).grid(row=2, column=0, columnspan=2, pady=10)

        tk.Button(self.frame_prestamos, text="Devolver Libro", command=self.devolver_libro).grid(row=3, column=0, columnspan=2, pady=10)

        # Área de texto para mostrar información
        self.info_text = tk.Text(self, height=10)
        self.info_text.pack(fill="both", expand="yes", padx=10, pady=10)

        tk.Button(self, text="Mostrar Libros", command=self.mostrar_libros).pack(side="left", padx=10, pady=10)
        tk.Button(self, text="Mostrar Usuarios", command=self.mostrar_usuarios).pack(side="left", padx=10, pady=10)
        tk.Button(self, text="Mostrar Préstamos", command=self.mostrar_prestamos).pack(side="right", padx=10, pady=10)

    def registrar_libro(self):
        titulo = self.titulo_entry.get()
        isbn = self.isbn_entry.get()
        nombre_autor = self.autor_entry.get()
        nombre_categoria = self.categoria_entry.get()

        if titulo and isbn and nombre_autor and nombre_categoria:
            autor = Autor(nombre_autor, "")  # Simplificación: apellido vacío
            categoria = Categoria(nombre_categoria)
            libro = Libro(titulo, isbn, autor, categoria)
            self.biblioteca.registrar_libro(libro)
            messagebox.showinfo("Éxito", "Libro registrado exitosamente")
            self.titulo_entry.delete(0, tk.END)
            self.isbn_entry.delete(0, tk.END)
            self.autor_entry.delete(0, tk.END)
            self.categoria_entry.delete(0, tk.END)
            self.mostrar_libros()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    def registrar_usuario(self):
        nombre = self.nombre_usuario_entry.get()
        apellido = self.apellido_usuario_entry.get()
        id_usuario = self.id_usuario_entry.get()

        if nombre and apellido and id_usuario:
            usuario = Usuario(nombre, apellido, int(id_usuario))
            self.biblioteca.registrar_usuario(usuario)
            messagebox.showinfo("Éxito", "Usuario registrado exitosamente")
            self.nombre_usuario_entry.delete(0, tk.END)
            self.apellido_usuario_entry.delete(0, tk.END)
            self.id_usuario_entry.delete(0, tk.END)
            self.mostrar_usuarios()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    def realizar_prestamo(self):
        titulo = self.titulo_prestamo_entry.get()
        id_usuario = self.id_usuario_prestamo_entry.get()

        libro = next((libro for libro in self.biblioteca.libros if libro.titulo == titulo), None)
        usuario = next((usuario for usuario in self.biblioteca.usuarios if usuario.id_usuario == int(id_usuario)), None)

        if libro and usuario:
            fecha_prestamo = datetime.now().strftime("%Y-%m-%d")
            self.biblioteca.realizar_prestamo(libro, usuario, fecha_prestamo)
            messagebox.showinfo("Éxito", "Préstamo realizado exitosamente")
            self.titulo_prestamo_entry.delete(0, tk.END)
            self.id_usuario_prestamo_entry.delete(0, tk.END)
            self.mostrar_prestamos()
        else:
            messagebox.showerror("Error", "Libro o Usuario no encontrados")

    def devolver_libro(self):
        titulo = self.titulo_prestamo_entry.get()
        id_usuario = self.id_usuario_prestamo_entry.get()

        prestamo = next((prestamo for prestamo in self.biblioteca.prestamos if prestamo.libro.titulo == titulo and prestamo.usuario.id_usuario == int(id_usuario)), None)

        if prestamo:
            fecha_devolucion = datetime.now().strftime("%Y-%m-%d")
            self.biblioteca.devolver_libro(prestamo, fecha_devolucion)
            messagebox.showinfo("Éxito", "Libro devuelto exitosamente")
            self.titulo_prestamo_entry.delete(0, tk.END)
            self.id_usuario_prestamo_entry.delete(0, tk.END)
            self.mostrar_prestamos()
        else:
            messagebox.showerror("Error", "Préstamo no encontrado")

    def mostrar_libros(self):
        self.info_text.delete(1.0, tk.END)
        libros_info = self.biblioteca.mostrar_libros()
        for info in libros_info:
            self.info_text.insert(tk.END, info + "\n")

    def mostrar_usuarios(self):
        self.info_text.delete(1.0, tk.END)
        usuarios_info = self.biblioteca.mostrar_usuarios()
        for info in usuarios_info:
            self.info_text.insert(tk.END, info + "\n")

    def mostrar_prestamos(self):
        self.info_text.delete(1.0, tk.END)
        prestamos_info = self.biblioteca.mostrar_prestamos()
        for info in prestamos_info:
            self.info_text.insert(tk.END, info + "\n")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
