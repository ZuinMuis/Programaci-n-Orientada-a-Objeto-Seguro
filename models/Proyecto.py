class Proyecto:
    """Clase Proyecto según el diagrama UML."""
    def __init__(self, id_proyecto: int, nombre: str, descripcion: str, fecha_inicio: str):
        self._id_proyecto = id_proyecto
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_inicio = fecha_inicio

    @property
    def id_proyecto(self) -> int:
        return self._id_proyecto

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def descripcion(self) -> str:
        return self._descripcion

    def crear(self):
        print(f"Proyecto '{self._nombre}' creado exitosamente.")

    def editar(self, nuevo_nombre: str, nueva_descripcion: str):
        self._nombre = nuevo_nombre
        self._descripcion = nueva_descripcion
        print(f"Proyecto ID {self._id_proyecto} modificado correctamente.")

    def eliminar(self):
        print(f"Proyecto '{self._nombre}' eliminado.")