from Usuarios import Administrador, Empleado
from Departamento import Departamento
from Proyecto import Proyecto
from Registro_Tiempo import Registro_Tiempo

if __name__ == "__main__":
    print("--- PROBANDO MODULOS EN CARPETAS SEPARADAS ---")
    
    dept = Departamento(1, "Tecnología", "Carlos Pérez")
    dept.crear()

    emp = Empleado(2, "ana@empresa.com", "pass123", 101, "Ana Gómez", "Calle 1", "912345678", "ana@empresa.com", "2026-01-10", 900000)
    
    registro = Registro_Tiempo(5001, "2026-10-19", 8.0, "Desarrollo de software")

    emp.asignarDepartamento(dept)
    emp.registrarHoras(registro)
    print("--- PRUEBA EXITOSA ---")



    