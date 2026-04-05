import tkinter as tk
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import TareaApp

if __name__ == "__main__":
    root = tk.Tk()
    servicio = TareaServicio()
    app = TareaApp(root, servicio)
    root.mainloop()  #fin
