import sys
from getpass import getpass

from models.Departamento import Departamento
from models.Proyecto import Proyecto
from models.Registro_Tiempo import Registro_Tiempo
from models.Usuarios import Administrador, Empleado

lista_departamentos = []
lista_proyectos = []
lista_empleados = []

def menu_principal():
    print("\n" + "="*50)
    print("      SISTEMA DE GESTIÓN - MENÚ INTUITIVO")
    print("="*50)
    print("1. 📋 Listar departamentos")
    print("2. ➕ Crear departamento")
    print("3. 📋 Listar proyectos")
    print("4. ➕ Crear proyecto")
    print("5. 📋 Listar empleados")
    print("6. ➕ Registrar empleado")
    print("7. 🛡️  Crear administrador")
    print("8. ⏱️  Registrar tiempo")
    print("0. 🚪 Salir")
    print("="*50)

def listar_departamentos():
    print("\n--- DEPARTAMENTOS ---")
    if lista_departamentos:
        print("📋 Departamentos existentes:")
        for idx, dept in enumerate(lista_departamentos, 1):
            print(f"  {idx}. ID: {dept.id_departamento} | Nombre: {dept.nombre} | Gerente: {dept.gerente}")
    else:
        print("No hay departamentos registrados en esta sesión.")

def gestionar_departamentos():
    print("\n--- CREAR DEPARTAMENTO ---")
    try:
        id_dept = int(input("Ingrese ID numérico del departamento: "))
        nombre = input("Ingrese nombre del departamento: ").strip()
        gerente = input("Ingrese nombre del gerente: ").strip()

        dept = Departamento(id_dept, nombre, gerente)
        lista_departamentos.append(dept)
        print(f"✅ Departamento '{dept.nombre}' creado.")
    except ValueError as error:
        print(f"❌ No se pudo crear el departamento: {error}")

def listar_proyectos():
    print("\n--- PROYECTOS ---")
    if lista_proyectos:
        print("📋 Proyectos existentes:")
        for idx, proj in enumerate(lista_proyectos, 1):
            print(f"  {idx}. ID: {proj.id_proyecto} | Nombre: {proj.nombre} | Inicio: {proj.fecha_inicio}")
    else:
        print("No hay proyectos registrados en esta sesión.")

def gestionar_proyectos():
    print("\n--- CREAR PROYECTO ---")
    try:
        id_proj = int(input("Ingrese ID numérico del proyecto: "))
        nombre = input("Ingrese nombre del proyecto: ").strip()
        descripcion = input("Ingrese descripción del proyecto: ").strip()
        fecha_inicio = input("Ingrese fecha de inicio (YYYY-MM-DD): ").strip()

        proyecto = Proyecto(id_proj, nombre, descripcion, fecha_inicio)
        lista_proyectos.append(proyecto)
        print(f"✅ Proyecto '{proyecto.nombre}' creado.")
    except ValueError as error:
        print(f"❌ No se pudo crear el proyecto: {error}")

def listar_empleados():
    print("\n--- EMPLEADOS ---")
    if lista_empleados:
        print("📋 Empleados registrados:")
        for idx, emp in enumerate(lista_empleados, 1):
            departamento = emp.departamento.nombre if emp.departamento else "Sin asignar"
            print(
                f"  {idx}. Nombre: {emp.nombre} | Correo: {emp.correo} "
                f"| Departamento: {departamento} | Salario: ${emp.salario:,.0f}"
            )
    else:
        print("No hay empleados registrados en esta sesión.")

def gestionar_empleados():
    print("\n--- REGISTRAR EMPLEADO ---")
    try:
        if not lista_departamentos:
            print("⚠️ Es recomendable crear un departamento primero.")

        id_user = int(input("Ingrese ID de usuario: "))
        correo = input("Ingrese correo institucional: ").strip()
        password = getpass("Ingrese contraseña: ")

        id_emp = int(input("Ingrese ID de empleado: "))
        nombre = input("Ingrese nombre completo: ").strip()
        direccion = input("Ingrese dirección: ").strip()
        telefono = input("Ingrese teléfono: ").strip()
        email = input("Ingrese email de contacto: ").strip()
        fecha_contrato = input("Ingrese fecha de contrato (YYYY-MM-DD): ").strip()
        salario = float(input("Ingrese salario: "))

        empleado = Empleado(
            id_usuario=id_user,
            correo=correo,
            password_plana=password,
            id_empleado=id_emp,
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email,
            fecha_contrato=fecha_contrato,
            salario=salario,
        )

        if lista_departamentos:
            print("\nSeleccione el departamento a asignar:")
            for idx, departamento in enumerate(lista_departamentos, 1):
                print(f"  {idx}. {departamento.nombre}")
            indice_departamento = int(input("Número de departamento: ")) - 1
            if not 0 <= indice_departamento < len(lista_departamentos):
                raise ValueError("Seleccion de departamento invalida.")
            empleado.asignar_departamento(lista_departamentos[indice_departamento])

        lista_empleados.append(empleado)
        print(f"✅ Empleado '{empleado.nombre}' registrado.")
    except ValueError as error:
        print(f"❌ No se pudo registrar el empleado: {error}")

def ingresar_administrador():
    print("\n--- CREAR ADMINISTRADOR ---")
    try:
        id_user = int(input("Ingrese ID de usuario: "))
        correo = input("Ingrese correo del administrador: ").strip()
        password = getpass("Ingrese contraseña: ")

        admin = Administrador(id_user, correo, password)
        print(f"✅ ¡Administrador '{admin.correo}' creado exitosamente!")
        print(admin.generar_informe())
    except ValueError:
        print("❌ Error: Los campos numéricos deben ingresarse correctamente.")

def registrar_tiempo_trabajo():
    print("\n--- REGISTRO DE TIEMPO ---")
    if not lista_empleados:
        print("❌ Primero debe registrar al menos un empleado en la opción 6.")
        return
    if not lista_proyectos:
        print("❌ Primero debe crear al menos un proyecto en la opción 4.")
        return

    try:
        # Seleccionar Empleado de forma intuitiva
        print("\nSeleccione el Empleado que registra horas:")
        for idx, e in enumerate(lista_empleados, 1):
            print(f"  {idx}. {e.nombre}")
        emp_idx = int(input("Elija el número de empleado: ")) - 1
        if not 0 <= emp_idx < len(lista_empleados):
            raise ValueError("Seleccion de empleado invalida.")
        empleado_seleccionado = lista_empleados[emp_idx]

        # Seleccionar Proyecto de forma intuitiva
        print("\nSeleccione el Proyecto asociado:")
        for idx, p in enumerate(lista_proyectos, 1):
            print(f"  {idx}. {p.nombre}")
        proj_idx = int(input("Elija el número de proyecto: ")) - 1
        if not 0 <= proj_idx < len(lista_proyectos):
            raise ValueError("Seleccion de proyecto invalida.")
        proyecto_seleccionado = lista_proyectos[proj_idx]

        id_reg = int(input("\nIngrese ID único del registro de tiempo: "))
        fecha = input("Ingrese fecha (YYYY-MM-DD): ").strip()
        horas = float(input("Ingrese cantidad de horas trabajadas: "))
        descripcion = input("Ingrese descripción de la tarea realizada: ").strip()

        reg = Registro_Tiempo(
            id_reg,
            fecha,
            horas,
            descripcion,
            empleado_seleccionado,
            proyecto_seleccionado,
        )
        
        print("\n--- RESULTADO DE LA ACCIÓN ---")
        empleado_seleccionado.registrar_horas(reg)
        print(f"📁 Proyecto asociado: {proyecto_seleccionado.nombre}")
        print(f"✅ ¡Registro guardado exitosamente!")

    except (ValueError, IndexError):
        print("❌ Error: Selección inválida o datos mal ingresados. Intente nuevamente.")

def main():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción del menú (0-8): ").strip()

        if opcion == "1":
            listar_departamentos()
        elif opcion == "2":
            gestionar_departamentos()
        elif opcion == "3":
            listar_proyectos()
        elif opcion == "4":
            gestionar_proyectos()
        elif opcion == "5":
            listar_empleados()
        elif opcion == "6":
            gestionar_empleados()
        elif opcion == "7":
            ingresar_administrador()
        elif opcion == "8":
            registrar_tiempo_trabajo()
        elif opcion == "0":
            print("\n👋 Saliendo del sistema. ¡Mucho éxito con tu proyecto!")
            sys.exit()
        else:
            print("❌ Opción no válida. Por favor, elija un número entre 0 y 8.")

if __name__ == "__main__":
    main()