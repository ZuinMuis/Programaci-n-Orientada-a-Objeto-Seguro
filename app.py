import sys
from Usuarios import Administrador, Empleado
from Departamento import Departamento
from Proyecto import Proyecto
from Registro_Tiempo import Registro_Tiempo

# Listas globales en memoria para almacenar los registros durante la ejecución
lista_departamentos = []
lista_proyectos = []
lista_empleados = []

def menu_principal():
    print("\n" + "="*50)
    print("      SISTEMA DE GESTIÓN - MENÚ INTUITIVO")
    print("="*50)
    print("1. 🏢 Ver y Crear Departamentos")
    print("2. 📁 Ver y Crear Proyectos")
    print("3. 👤 Ver y Registrar Empleados")
    print("4. 🛡️  Crear Administrador")
    print("5. ⏱️  Registrar Tiempo (Asociado a Empleado/Proyecto)")
    print("0. 🚪 Salir")
    print("="*50)

def gestionar_departamentos():
    print("\n--- GESTIÓN DE DEPARTAMENTOS ---")
    if lista_departamentos:
        print("📋 Departamentos existentes:")
        for idx, dept in enumerate(lista_departamentos, 1):
            print(f"  {idx}. ID: {dept.id_departamento} | Nombre: {dept.nombre} | Gerente: {dept.gerente}")
    else:
        print("⚠️ No hay departamentos creados todavía.")
    
    op = input("\n¿Desea crear un nuevo departamento? (s/n): ").strip().lower()
    if op == 's':
        try:
            id_dept = int(input("Ingrese ID numérico del departamento: "))
            nombre = input("Ingrese nombre del departamento: ").strip()
            gerente = input("Ingrese nombre del gerente: ").strip()

            dept = Departamento(id_dept, nombre, gerente)
            lista_departamentos.append(dept)
            print(f"✅ ¡Departamento '{dept.nombre}' creado y guardado con éxito!")
        except ValueError as e:
            print(f"❌ Error en el formato de los datos: {e}")

def gestionar_proyectos():
    print("\n--- GESTIÓN DE PROYECTOS ---")
    if lista_proyectos:
        print("📋 Proyectos existentes:")
        for idx, proj in enumerate(lista_proyectos, 1):
            print(f"  {idx}. ID: {proj.id_proyecto} | Nombre: {proj.nombre} | Inicio: {proj._fecha_inicio}")
    else:
        print("⚠️ No hay proyectos creados todavía.")
    
    op = input("\n¿Desea crear un nuevo proyecto? (s/n): ").strip().lower()
    if op == 's':
        try:
            id_proj = int(input("Ingrese ID numérico del proyecto: "))
            nombre = input("Ingrese nombre del proyecto: ").strip()
            descripcion = input("Ingrese descripción del proyecto: ").strip()
            fecha_inicio = input("Ingrese fecha de inicio (YYYY-MM-DD): ").strip()

            proj = Proyecto(id_proj, nombre, descripcion, fecha_inicio)
            lista_proyectos.append(proj)
            print(f"✅ ¡Proyecto '{proj.nombre}' creado y guardado con éxito!")
        except ValueError as e:
            print(f"❌ Error en el formato de los datos: {e}")

def gestionar_empleados():
    print("\n--- GESTIÓN DE EMPLEADOS ---")
    if lista_empleados:
        print("📋 Empleados registrados:")
        for idx, emp in enumerate(lista_empleados, 1):
            print(f"  {idx}. Nombre: {emp.nombre} | Correo: {emp.correo} | Salario: ${emp.salario:,.0f}")
    else:
        print("⚠️ No hay empleados registrados todavía.")

    op = input("\n¿Desea registrar un nuevo empleado? (s/n): ").strip().lower()
    if op == 's':
        try:
            if not lista_departamentos:
                print("⚠️ Advertencia: Es recomendable crear un departamento primero.")

            id_user = int(input("Ingrese ID de usuario: "))
            correo = input("Ingrese correo institucional: ").strip()
            password = input("Ingrese contraseña: ").strip()
            
            id_emp = int(input("Ingrese ID de empleado: "))
            nombre = input("Ingrese nombre completo: ").strip()
            direccion = input("Ingrese dirección: ").strip()
            telefono = input("Ingrese teléfono: ").strip()
            email = input("Ingrese email de contacto: ").strip()
            fecha_contrato = input("Ingrese fecha de contrato (YYYY-MM-DD): ").strip()
            salario = float(input("Ingrese salario: "))

            emp = Empleado(
                id_usuario=id_user, correo=correo, password_plana=password,
                id_empleado=id_emp, nombre=nombre, direccion=direccion,
                telefono=telefono, email=email, fecha_contrato=fecha_contrato, salario=salario
            )
            
            # Si hay departamentos, permitimos asignarlo de forma intuitiva
            if lista_departamentos:
                print("\nSeleccione el departamento a asignar:")
                for idx, d in enumerate(lista_departamentos, 1):
                    print(f"  {idx}. {d.nombre}")
                op_dept = int(input("Número de departamento: ")) - 1
                if 0 <= op_dept < len(lista_departamentos):
                    emp.asignarDepartamento(lista_departamentos[op_dept])

            lista_empleados.append(emp)
            print(f"✅ ¡Empleado '{emp.nombre}' registrado con éxito!")
        except ValueError as e:
            print(f"❌ Error en los datos ingresados: {e}")

def ingresar_administrador():
    print("\n--- CREAR ADMINISTRADOR ---")
    try:
        id_user = int(input("Ingrese ID de usuario: "))
        correo = input("Ingrese correo del administrador: ").strip()
        password = input("Ingrese contraseña: ").strip()

        admin = Administrador(id_user, correo, password)
        print(f"✅ ¡Administrador '{admin.correo}' creado exitosamente!")
        admin.generarInforme()
    except ValueError:
        print("❌ Error: Los campos numéricos deben ingresarse correctamente.")

def registrar_tiempo_trabajo():
    print("\n--- REGISTRO DE TIEMPO ---")
    if not lista_empleados:
        print("❌ Primero debe registrar al menos un Empleado en la opción 3.")
        return
    if not lista_proyectos:
        print("❌ Primero debe crear al menos un Proyecto en la opción 2.")
        return

    try:
        # Seleccionar Empleado de forma intuitiva
        print("\nSeleccione el Empleado que registra horas:")
        for idx, e in enumerate(lista_empleados, 1):
            print(f"  {idx}. {e.nombre}")
        emp_idx = int(input("Elija el número de empleado: ")) - 1
        empleado_seleccionado = lista_empleados[emp_idx]

        # Seleccionar Proyecto de forma intuitiva
        print("\nSeleccione el Proyecto asociado:")
        for idx, p in enumerate(lista_proyectos, 1):
            print(f"  {idx}. {p.nombre}")
        proj_idx = int(input("Elija el número de proyecto: ")) - 1
        proyecto_seleccionado = lista_proyectos[proj_idx]

        id_reg = int(input("\nIngrese ID único del registro de tiempo: "))
        fecha = input("Ingrese fecha (YYYY-MM-DD): ").strip()
        horas = float(input("Ingrese cantidad de horas trabajadas: "))
        descripcion = input("Ingrese descripción de la tarea realizada: ").strip()

        reg = Registro_Tiempo(id_reg, fecha, horas, descripcion)
        
        print("\n--- RESULTADO DE LA ACCIÓN ---")
        empleado_seleccionado.registrarHoras(reg)
        print(f"📁 Proyecto asociado: {proyecto_seleccionado.nombre}")
        print(f"✅ ¡Registro guardado exitosamente!")

    except (ValueError, IndexError):
        print("❌ Error: Selección inválida o datos mal ingresados. Intente nuevamente.")

def main():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción del menú (0-5): ").strip()

        if opcion == "1":
            gestionar_departamentos()
        elif opcion == "2":
            gestionar_proyectos()
        elif opcion == "3":
            gestionar_empleados()
        elif opcion == "4":
            ingresar_administrador()
        elif opcion == "5":
            registrar_tiempo_trabajo()
        elif opcion == "0":
            print("\n👋 Saliendo del sistema. ¡Mucho éxito con tu proyecto!")
            sys.exit()
        else:
            print("❌ Opción no válida. Por favor, elija un número entre 0 y 5.")

if __name__ == "__main__":
    main()