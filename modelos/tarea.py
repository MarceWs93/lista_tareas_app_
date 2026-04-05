class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False # Estado inicial de toda tarea nueva

    def marcar_como_completada(self):
        # Cambia el estado lógico de la tarea
        self.completada = True