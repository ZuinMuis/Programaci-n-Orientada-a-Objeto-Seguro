import hashlib

class Usuario:
    def __init__(self, id_usuario: int, correo: str, password_plana: str, rol: str):
        self._id_usuario = id_usuario
        self._correo = correo
        self._password_hash = hashlib.sha256(password_plana.encode('utf-8')).hexdigest()
        self._rol = rol

    @property
    def correo(self) -> str:
        return self._correo

    def registrarHoras(self, registro_tiempo):
        print(f"[{self._rol}] {self._correo}: Horas registradas correctamente.")

    def asignarDepartamento(self, departamento):
        print(f"[{self._rol}] {self._correo}: Asignado al departamento.")


class Administrador(Usuario):
    def __init__(self, id_usuario: int, correo: str, password_plana: str):
        super().__init__(
            id_usuario=id_usuario, 
            correo=correo, 
            password_plana=password_plana, 
            rol="Administrador"
        )

    def gestionar(self, entidad: str):
        print(f"El Administrador {self._correo} está gestionando: {entidad}")

    def generarInforme(self) -> str:
        informe = f"--- INFORME DEL SISTEMA ---\nGenerado por: {self._correo}\nRol: {self._rol}"
        print(informe)
        return informe