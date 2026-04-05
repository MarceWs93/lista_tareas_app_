from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        # Encapsulamiento de la lista de tareas en memoria
        self._tareas = []

    def añadir_tarea(self, descripcion):
        if descripcion.strip():
            nueva = Tarea(descripcion)
            self._tareas.append(nueva)
            return True
        return False

    def eliminar_tarea(self, indice):
        # Elimina por posición en la lista
        if 0 <= indice < len(self._tareas):
            del self._tareas[indice]
            return True
        return False

    def completar_tarea(self, indice):
        # Cambia el estado de una tarea específica
        if 0 <= indice < len(self._tareas):
            self._tareas[indice].marcar_como_completada()
            return True
        return False

    def obtener_todas(self):
        return self._tareas
