import tkinter as tk
from tkinter import messagebox, ttk

class TareaApp:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio
        self.root.title("Gestor de Tareas Semanales")
        self.root.geometry("400x450")

        self.tarea_var = tk.StringVar()
        self._setup_ui()
        self._setup_bindings()

    def _setup_ui(self):
        # Campo de entrada
        frame_top = tk.Frame(self.root, pady=10)
        frame_top.pack(fill="x")

        self.entry = tk.Entry(frame_top, textvariable=self.tarea_var, width=30)
        self.entry.pack(side="left", padx=10)

        tk.Button(frame_top, text="Añadir", command=self._añadir).pack(side="left")

        # Lista de tareas (Treeview)
        self.tabla = ttk.Treeview(self.root, columns=("Estado", "Descripción"), show="headings")
        self.tabla.heading("Estado", text="Estado")
        self.tabla.heading("Descripción", text="Tarea")
        self.tabla.column("Estado", width=80)
        self.tabla.pack(padx=10, pady=10, fill="both", expand=True)

        # Botones de acción
        frame_bot = tk.Frame(self.root, pady=10)
        frame_bot.pack()

        tk.Button(frame_bot, text="Marcar Completada", command=self._completar, bg="#d1e7dd").pack(side="left", padx=5)
        tk.Button(frame_bot, text="Eliminar", command=self._eliminar, bg="#f8d7da").pack(side="left", padx=5)

    def _setup_bindings(self):
        # Eventos de teclado
        self.entry.bind("<Return>", lambda event: self._añadir())
        self.root.bind("<c>", lambda event: self._completar())
        self.root.bind("<d>", lambda event: self._eliminar())
        self.root.bind("<Delete>", lambda event: self._eliminar())
        self.root.bind("<Escape>", lambda event: self.root.quit())

        # Evento de ratón
        self.tabla.bind("<Double-1>", lambda event: self._completar())

    def _añadir(self):
        if self.servicio.añadir_tarea(self.tarea_var.get()):
            self._actualizar_lista()
            self.tarea_var.set("")  # Limpia el campo
        else:
            messagebox.showwarning("Aviso", "La tarea no puede estar vacía")

    def _completar(self):
        seleccion = self.tabla.selection()
        if seleccion:
            indice = self.tabla.index(seleccion[0])
            self.servicio.completar_tarea(indice)
            self._actualizar_lista()

    def _eliminar(self):
        seleccion = self.tabla.selection()
        if seleccion:
            indice = self.tabla.index(seleccion[0])
            self.servicio.eliminar_tarea(indice)
            self._actualizar_lista()

    def _actualizar_lista(self):
        # Borra y repinta la tabla con feedback visual
        for i in self.tabla.get_children():
            self.tabla.delete(i)

        for t in self.servicio.obtener_todas():
            estado = "[Hecho]" if t.completada else "[Pendiente]"
            self.tabla.insert("", "end", values=(estado, t.descripcion))
