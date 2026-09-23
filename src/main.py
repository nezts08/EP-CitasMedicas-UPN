from utils.citas import (
    registrar_paciente_menu,
    registrar_medico_menu,
    buscar_por_codigo_menu,
    agendar_cita_menu,
    registrar_atencion_menu,
    buscar_por_especialidad_menu,
    consultar_historial_citas_menu,
)


def menu_principal():
    while True:
        print("\n========================================")
        print("    SISTEMA KAWSAY - MENÚ PRINCIPAL")
        print("========================================")
        print("1. Registrar Paciente (RF01)")
        print("2. Registrar Médico (RF02)")
        print("3. Buscar por Código (RF03)")
        print("4. Programar Cita (RF04)")
        print("5. Registrar Atención / Diagnóstico (RF05)")
        print("6. Buscar Médicos por Especialidad (Consulta Funcional)")
        print("7. Consultar Historial de Citas por Paciente")
        print("8. Salir del Sistema")

        opcion = input("\nSeleccione una opción (1-8): ").strip()

        if opcion == "1":
            registrar_paciente_menu()
        elif opcion == "2":
            registrar_medico_menu()
        elif opcion == "3":
            buscar_por_codigo_menu()
        elif opcion == "4":
            agendar_cita_menu()
        elif opcion == "5":
            registrar_atencion_menu()
        elif opcion == "6":
            buscar_por_especialidad_menu()
        elif opcion == "7":
            consultar_historial_citas_menu()
        elif opcion == "8":
            print("\nSaliendo del sistema Kawsay... ¡Hasta luego!")
            break
        else:
            print("\n[!] Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu_principal()
