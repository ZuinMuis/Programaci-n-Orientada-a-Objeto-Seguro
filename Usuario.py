import hashlib

class Usuario:
   
    def __init__(self, id_usuario: int, correo: str, password_plana: str, rol: str):
        self._id_usuario = id_usuario
        self._correo = correo
        self._password_hash = self._hash_password(password_plana)
        self._rol = rol

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

   
    @property
    def id_usuario(self) -> int:
        return self._id_usuario

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, nuevo_correo: str):
        if "@" in nuevo_correo and "." in nuevo_correo:
            self._correo = nuevo_correo
        else:
            raise ValueError("El correo electrónico ingresado no tiene un formato válido.")

    @property
    def rol(self) -> str:
        return self._rol

    def registrarHoras(self, registro_tiempo):
        """Registra una instancia de Registro_Tiempo asociada al usuario."""
        print(f"[{self._rol}] {self._correo}: Horas registradas correctamente.")

    def asignarDepartamento(self, departamento):
        """Asigna un departamento al usuario."""
        print(f"[{self._rol}] {self._correo}: Asignado al departamento '{departamento.nombre}'.")

    def verificar_password(self, password: str) -> bool:
        """Valida si la contraseña ingresada coincide con el hash almacenado."""
        return self._password_hash == self._hash_password(password)


class Administrador(Usuario):
   
    def __init__(self, id_usuario: int, correo: str, password_plana: str):
        super().__init__(id_usuario=id_usuario, correo=correo, password_plana=password_plana, rol="Administrador")

    def gestionar(self):
        print(f"El Administrador {self.correo} está realizando labores de gestión.")

    def generarInforme(self) -> str:
        return f"Informe del sistema generado por el Administrador: {self.correo}"