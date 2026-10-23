from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Proyecto import Proyecto
    from .Usuarios import Empleado


class Registro_Tiempo:
    """Asocia las horas trabajadas con un empleado y un proyecto."""

    def __init__(
        self,
        id_registro: int,
        fecha: str,
        horas: float,
        descripcion: str,
        empleado: Empleado,
        proyecto: Proyecto,
    ) -> None:
        if id_registro <= 0:
            raise ValueError("El ID del registro debe ser positivo.")
        self._id_registro = id_registro
        self._fecha = self._validar_fecha(fecha)
        self.horas = horas
        self._descripcion = self._validar_texto(descripcion)
        self._empleado = empleado
        self._proyecto = proyecto

    @staticmethod
    def _validar_fecha(valor: str) -> str:
        try:
            return date.fromisoformat(valor).isoformat()
        except ValueError as error:
            raise ValueError("La fecha debe tener formato YYYY-MM-DD.") from error

    @staticmethod
    def _validar_texto(valor: str) -> str:
        valor = valor.strip()
        if not valor:
            raise ValueError("La descripcion no puede estar vacia.")
        return valor

    @property
    def id_registro(self) -> int:
        return self._id_registro

    @property
    def fecha(self) -> str:
        return self._fecha

    @property
    def horas(self) -> float:
        return self._horas

    @horas.setter
    def horas(self, cantidad: float) -> None:
        if cantidad <= 0:
            raise ValueError("Las horas registradas deben ser mayores a 0.")
        self._horas = cantidad

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @property
    def empleado(self) -> Empleado:
        return self._empleado

    @property
    def proyecto(self) -> Proyecto:
        return self._proyecto

    def modificar(self, nuevas_horas: float, nueva_descripcion: str) -> None:
        self.horas = nuevas_horas
        self._descripcion = self._validar_texto(nueva_descripcion)