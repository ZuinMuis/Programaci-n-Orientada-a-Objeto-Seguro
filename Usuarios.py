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
        super().__init__(id_usuario=id_usuario, correo=correo, password_plana=password_plana, rol="Administrador")

    def gestionar(self, entidad: str):
        print(f"El Administrador {self._correo} está gestionando: {entidad}")

    def generarInforme(self) -> str:
        informe = f"--- INFORME ---\nGenerado por Administrador: {self._correo}"
        print(informe)
        return informe


class Empleado(Usuario):
    def __init__(self, id_usuario: int, correo: str, password_plana: str, 
                 id_empleado: int, nombre: str, direccion: str, telefono: str, 
                 email: str, fecha_contrato: str, salario: float):
        super().__init__(id_usuario=id_usuario, correo=correo, password_plana=password_plana, rol="Empleado")
        self._id_empleado = id_empleado
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._email = email
        self._fecha_contrato = fecha_contrato
        self._salario = salario

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def salario(self) -> float:
        return self._salario

    def registrarHoras(self, registro_tiempo):
        print(f"El empleado {self._nombre} ha registrado sus horas.")

    def asignarDepartamento(self, departamento):
        print(f"El empleado {self._nombre} fue asignado al departamento: {departamento.nombre}")