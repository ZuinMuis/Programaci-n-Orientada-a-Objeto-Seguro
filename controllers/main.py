from models.Departamento import Departamento
from models.Proyecto import Proyecto
from models.Registro_Tiempo import Registro_Tiempo
from models.Usuarios import Administrador, Empleado

if __name__ == "__main__":
    print("--- PROBANDO MODULOS EN CARPETAS SEPARADAS ---")
    
    dept = Departamento(1, "Tecnología", "Carlos Pérez")
    emp = Empleado(2, "ana@empresa.com", "pass123", 101, "Ana Gómez", "Calle 1", "912345678", "ana@empresa.com", "2026-01-10", 900000)

    proyecto = Proyecto(1, "Sistema", "Desarrollo de software", "2026-01-10")
    registro = Registro_Tiempo(5001, "2026-10-19", 8.0, "Desarrollo de software", emp, proyecto)

    emp.asignar_departamento(dept)
    emp.registrar_horas(registro)
    print(f"Departamento: {emp.departamento.nombre if emp.departamento else 'Sin asignar'}")
    print(f"Proyecto del registro: {registro.proyecto.nombre}")
    print("--- PRUEBA EXITOSA ---")



    