class Departamento:
    """Clase Departamento según el diagrama UML."""
    def __init__(self, id_departamento: int, nombre: str, gerente: str):
        self._id_departamento = id_departamento
        self._nombre = nombre
        self._gerente = gerente

    @property
    def id_departamento(self) -> int:
        return self._id_departamento

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        if nuevo_nombre.strip():
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre del departamento no puede estar vacío.")

    @property
    def gerente(self) -> str:
        return self._gerente

    def crear(self):
        print(f"Departamento '{self._nombre}' creado exitosamente.")

    def editar(self, nuevo_nombre: str, nuevo_gerente: str):
        self.nombre = nuevo_nombre
        self._gerente = nuevo_gerente
        print(f"Departamento ID {self._id_departamento} actualizado.")

    def buscar(self, id_dept: int) -> bool:
        return self._id_departamento == id_dept

    def eliminar(self):
        print(f"Departamento '{self._nombre}' eliminado del sistema.")