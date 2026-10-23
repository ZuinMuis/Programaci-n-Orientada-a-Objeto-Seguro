class Registro_Tiempo:
    """Clase Registro_Tiempo según el diagrama UML."""
    def __init__(self, id_registro: int, fecha: str, horas: float, descripcion: str):
        self._id_registro = id_registro
        self._fecha = fecha
        self._horas = horas
        self._descripcion = descripcion

    @property
    def id_registro(self) -> int:
        return self._id_registro

    @property
    def horas(self) -> float:
        return self._horas

    @horas.setter
    def horas(self, cantidad: float):
        if cantidad > 0:
            self._horas = cantidad
        else:
            raise ValueError("Las horas registradas deben ser mayores a 0.")

    def registrar(self):
        print("Registro de tiempo guardado exitosamente.")

    def modificar(self, nuevas_horas: float, nueva_descripcion: str):
        self.horas = nuevas_horas
        self._descripcion = nueva_descripcion
        print(f"Registro ID {self._id_registro} modificado: {self._horas}h")

    def eliminar(self):
        print(f"Registro de tiempo ID {self._id_registro} eliminado.")