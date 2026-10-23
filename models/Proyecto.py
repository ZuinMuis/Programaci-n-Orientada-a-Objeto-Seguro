from datetime import date


class Proyecto:
    """Clase Proyecto según el diagrama UML."""
    def __init__(self, id_proyecto: int, nombre: str, descripcion: str, fecha_inicio: str):
        self._id_proyecto = id_proyecto
        self._nombre = self._validar_texto(nombre, "nombre")
        self._descripcion = self._validar_texto(descripcion, "descripcion")
        self._fecha_inicio = self._validar_fecha(fecha_inicio)

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        valor = valor.strip()
        if not valor:
            raise ValueError(f"El {campo} del proyecto no puede estar vacio.")
        return valor

    @staticmethod
    def _validar_fecha(valor: str) -> str:
        try:
            return date.fromisoformat(valor).isoformat()
        except ValueError as error:
            raise ValueError("La fecha debe tener formato YYYY-MM-DD.") from error

    @property
    def id_proyecto(self) -> int:
        return self._id_proyecto

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @property
    def fecha_inicio(self) -> str:
        return self._fecha_inicio

    def editar(self, nuevo_nombre: str, nueva_descripcion: str) -> None:
        self._nombre = self._validar_texto(nuevo_nombre, "nombre")
        self._descripcion = self._validar_texto(nueva_descripcion, "descripcion")