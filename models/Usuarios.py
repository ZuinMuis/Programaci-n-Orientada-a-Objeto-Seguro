from __future__ import annotations

import hashlib
import hmac
import os
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Departamento import Departamento
    from .Registro_Tiempo import Registro_Tiempo


class Usuario:
    """Clase base con identidad, correo y credenciales protegidas."""

    _SCRYPT_N = 2**14
    _SCRYPT_R = 8
    _SCRYPT_P = 1

    def __init__(self, id_usuario: int, correo: str, password_plana: str) -> None:
        if id_usuario <= 0:
            raise ValueError("El ID de usuario debe ser positivo.")
        correo = correo.strip().lower()
        if "@" not in correo or correo.startswith("@") or correo.endswith("@"):
            raise ValueError("El correo no tiene un formato valido.")
        if not password_plana:
            raise ValueError("La contrasena no puede estar vacia.")
        self._id_usuario = id_usuario
        self._correo = correo
        self._password_salt = os.urandom(16)
        self._password_hash = self._hash_password(password_plana, self._password_salt)

    @classmethod
    def _hash_password(cls, password: str, salt: bytes) -> bytes:
        return hashlib.scrypt(
            password.encode("utf-8"),
            salt=salt,
            n=cls._SCRYPT_N,
            r=cls._SCRYPT_R,
            p=cls._SCRYPT_P,
        )

    @property
    def id_usuario(self) -> int:
        return self._id_usuario

    @property
    def correo(self) -> str:
        return self._correo

    @property
    def rol(self) -> str:
        return self.__class__.__name__

    def verificar_contrasena(self, password: str) -> bool:
        hash_ingresado = self._hash_password(password, self._password_salt)
        return hmac.compare_digest(self._password_hash, hash_ingresado)


class Administrador(Usuario):
    """Usuario con permisos para administrar el sistema."""

    def gestionar(self, entidad: str) -> str:
        entidad = entidad.strip()
        if not entidad:
            raise ValueError("Debe indicar la entidad que se gestionara.")
        return f"El administrador {self.correo} gestiona: {entidad}"

    def generar_informe(self) -> str:
        return f"--- INFORME ---\nGenerado por administrador: {self.correo}"


class Empleado(Usuario):
    """Usuario que pertenece opcionalmente a un departamento y registra horas."""

    def __init__(
        self,
        id_usuario: int,
        correo: str,
        password_plana: str,
        id_empleado: int,
        nombre: str,
        direccion: str,
        telefono: str,
        email: str,
        fecha_contrato: str,
        salario: float,
    ) -> None:
        super().__init__(id_usuario, correo, password_plana)
        if id_empleado <= 0:
            raise ValueError("El ID de empleado debe ser positivo.")
        if salario < 0:
            raise ValueError("El salario no puede ser negativo.")
        email = email.strip().lower()
        if "@" not in email or email.startswith("@") or email.endswith("@"):
            raise ValueError("El email de contacto no tiene un formato valido.")
        try:
            self._fecha_contrato = date.fromisoformat(fecha_contrato).isoformat()
        except ValueError as error:
            raise ValueError("La fecha de contrato debe tener formato YYYY-MM-DD.") from error
        self._id_empleado = id_empleado
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._email = email
        self._salario = salario
        self._departamento: Departamento | None = None
        self._registros_tiempo: list[Registro_Tiempo] = []

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        valor = valor.strip()
        if not valor:
            raise ValueError(f"El {campo} no puede estar vacio.")
        return valor

    @property
    def id_empleado(self) -> int:
        return self._id_empleado

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def salario(self) -> float:
        return self._salario

    @property
    def departamento(self) -> Departamento | None:
        return self._departamento

    @property
    def registros_tiempo(self) -> tuple[Registro_Tiempo, ...]:
        return tuple(self._registros_tiempo)

    def asignar_departamento(self, departamento: Departamento | None) -> None:
        if self._departamento is departamento:
            return
        if self._departamento is not None:
            self._departamento._quitar_empleado(self)
        self._departamento = departamento
        if departamento is not None:
            departamento._agregar_empleado(self)

    def registrar_horas(self, registro_tiempo: Registro_Tiempo) -> None:
        if registro_tiempo.empleado is not self:
            raise ValueError("El registro pertenece a otro empleado.")
        if registro_tiempo not in self._registros_tiempo:
            self._registros_tiempo.append(registro_tiempo)


