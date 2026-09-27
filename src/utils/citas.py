from classes.paciente import Paciente
from classes.medico import Medico
from classes.cita import Cita
from datetime import datetime

pacientes = []
medicos = []
historial_citas = []
secuencia_citas = 1


def crear_persona(tipo: str, codigo: str, nombre: str, extra):
    tipo = tipo.lower().strip()
    if tipo == "paciente":
        return Paciente(codigo, nombre, int(extra))
    elif tipo == "medico":
        return Medico(codigo, nombre, str(extra))
    else:
        raise ValueError(f"Tipo de persona no soportado: {tipo}")


def registrar_paciente_menu():
    print("\n--- REGISTRAR PACIENTE (RF01) ---")
    try:
        codigo = input("Ingrese código del paciente (ej. P001): ").strip()
        if not codigo:
            print("[ERROR] El código no puede estar vacío.")
            return

        existe = list(filter(lambda p: p.codigo.lower() == codigo.lower(), pacientes))
        if existe:
            print(f"[ERROR] El paciente con código {codigo} ya existe.")
            return

        nombre = input("Ingrese nombre completo: ").strip()
        edad_str = input("Ingrese edad (0 a 120): ").strip()
        edad = int(edad_str)

        nuevo_paciente = crear_persona("paciente", codigo, nombre, edad)

        pacientes.append(nuevo_paciente)
        print(f"[OK] {nuevo_paciente.resumen()} registrado correctamente.")

    except ValueError as err:
        print(f"[ERROR] Entrada inválida o fuera de rango: {err}")


def registrar_medico_menu():
    print("\n--- REGISTRAR MÉDICO (RF02) ---")
    codigo = input("Ingrese código del médico (ej. M001): ").strip()
    if not codigo:
        print("[ERROR] El código no puede estar vacío.")
        return

    existe = list(filter(lambda m: m.codigo.lower() == codigo.lower(), medicos))
    if existe:
        print(f"[ERROR] El médico con código {codigo} ya existe.")
        return

    nombre = input("Ingrese nombre del médico: ").strip()
    especialidad = input("Ingrese especialidad: ").strip()
    if not especialidad:
        print("[ERROR] La especialidad no puede estar vacía.")
        return

    nuevo_medico = crear_persona("medico", codigo, nombre, especialidad)

    medicos.append(nuevo_medico)
    print(f"[OK] {nuevo_medico.resumen()} registrado correctamente.")


def buscar_por_codigo_menu():
    print("\n--- BUSCAR POR CÓDIGO (RF03) ---")
    codigo = input("Ingrese el código a buscar (Paciente o Médico): ").strip()

    p_encontrado = list(filter(lambda p: p.codigo.lower() == codigo.lower(), pacientes))
    m_encontrado = list(filter(lambda m: m.codigo.lower() == codigo.lower(), medicos))

    if p_encontrado:
        print(f"[ENCONTRADO - PACIENTE]: {p_encontrado[0].resumen()}")
    elif m_encontrado:
        print(f"[ENCONTRADO - MÉDICO]: {m_encontrado[0].resumen()}")
    else:
        print(
            f"[ERROR] No se encontró ninguna entidad registrada con el código '{codigo}'."
        )


def agendar_cita_menu():
    global secuencia_citas
    print("\n--- PROGRAMAR CITA (RF04) ---")

    cod_paciente = input("Ingrese código del paciente: ").strip()
    p_encontrado = list(
        filter(lambda p: p.codigo.lower() == cod_paciente.lower(), pacientes)
    )
    if not p_encontrado:
        print(
            f"[ERROR] No existe paciente con código '{cod_paciente}'. Debe registrarlo primero."
        )
        return

    cod_medico = input("Ingrese código del médico: ").strip()
    m_encontrado = list(
        filter(lambda m: m.codigo.lower() == cod_medico.lower(), medicos)
    )
    if not m_encontrado:
        print(
            f"[ERROR] No existe médico con código '{cod_medico}'. Debe registrarlo primero."
        )
        return

    fecha = input("Ingrese fecha (o presione Enter para fecha actual): ").strip()
    if not fecha:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    motivo = input("Ingrese motivo de la consulta: ").strip()

    cod_cita = f"C{secuencia_citas:03d}"

    nueva_cita = Cita(cod_cita, p_encontrado[0], m_encontrado[0], fecha, motivo)
    historial_citas.append(nueva_cita)
    secuencia_citas += 1

    print(
        f"[OK] Cita {cod_cita} programada exitosamente para {p_encontrado[0].nombre}."
    )


def registrar_atencion_menu():
    print("\n--- REGISTRAR ATENCIÓN / HISTORIAL (RF05) ---")
    cod_cita = input("Ingrese el código de la cita (ej. C001): ").strip()

    citas_filtradas = list(
        filter(lambda c: c.codigo.lower() == cod_cita.lower(), historial_citas)
    )

    if not citas_filtradas:
        print(f"[ERROR] No se encontró la cita con código '{cod_cita}'.")
        return

    cita = citas_filtradas[0]
    diagnostico = input("Ingrese el diagnóstico / nota de atención: ").strip()
    cita.completar_atencion(diagnostico)
    print(f"[OK] Atención registrada para la cita {cita.codigo}.")


def buscar_por_especialidad_menu():
    print("\n--- BÚSQUEDA DE MÉDICOS POR ESPECIALIDAD (CONSULTA FUNCIONAL) ---")
    especialidad = input("Ingrese la especialidad a buscar: ").strip()

    medicos_encontrados = list(
        filter(lambda m: especialidad.lower() in m.especialidad.lower(), medicos)
    )

    if not medicos_encontrados:
        print(
            f"No se encontraron médicos registrados en la especialidad '{especialidad}'."
        )
    else:
        print(f"\nSe encontraron {len(medicos_encontrados)} médico(s):")
        for m in medicos_encontrados:
            print(f" - {m.resumen()}")


def consultar_historial_citas_menu():
    print("\n--- CONSULTAR HISTORIAL DE CITAS POR PACIENTE ---")
    cod_paciente = input("Ingrese código del paciente a consultar: ").strip()

    citas_paciente = list(
        filter(
            lambda c: c.paciente.codigo.lower() == cod_paciente.lower(), historial_citas
        )
    )

    if not citas_paciente:
        print(f"No se encontraron citas agendadas para el paciente '{cod_paciente}'.")
    else:
        print(f"\nSe encontraron {len(citas_paciente)} cita(s):")
        for c in citas_paciente:
            print("----------------------------------------")
            print(c.resumen())
        print("----------------------------------------")
