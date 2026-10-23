from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Usuarios import Empleado


class Departamento:
    """Agrupa empleados y mantiene los datos propios de un departamento."""

    def __init__(self, id_departamento: int, nombre: str, gerente: str) -> None:
        if id_departamento <= 0:
            raise ValueError("El ID del departamento debe ser positivo.")
        self._id_departamento = id_departamento
        self._nombre = self._validar_texto(nombre, "nombre")
        self._gerente = self._validar_texto(gerente, "gerente")
        self._empleados: list[Empleado] = []

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        valor = valor.strip()
        if not valor:
            raise ValueError(f"El {campo} del departamento no puede estar vacio.")
        return valor

    @property
    def id_departamento(self) -> int:
        return self._id_departamento

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self._nombre = self._validar_texto(nuevo_nombre, "nombre")

    @property
    def gerente(self) -> str:
        return self._gerente

    @property
    def empleados(self) -> tuple[Empleado, ...]:
        return tuple(self._empleados)

    def _agregar_empleado(self, empleado: Empleado) -> None:
        if empleado not in self._empleados:
            self._empleados.append(empleado)

    def _quitar_empleado(self, empleado: Empleado) -> None:
        if empleado in self._empleados:
            self._empleados.remove(empleado)

    def editar(self, nuevo_nombre: str, nuevo_gerente: str):
        self.nombre = nuevo_nombre
        self._gerente = nuevo_gerente
        print(f"Departamento ID {self._id_departamento} actualizado.")

    def buscar(self, id_dept: int) -> bool:
        return self._id_departamento == id_dept

    def eliminar(self):
        print(f"Departamento '{self._nombre}' eliminado del sistema.")