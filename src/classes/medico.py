class Medico:
    def __init__(self, codigo: str, nombre: str, especialidad: str):
        self._codigo = str(codigo).strip()
        self._nombre = str(nombre).strip()
        self._especialidad = str(especialidad).strip()

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def especialidad(self) -> str:
        return self._especialidad

    def resumen(self) -> str:
        return f"Médico [Código: {self._codigo}] Dr(a). {self._nombre} - Especialidad: {self._especialidad}" # Esto nos devuelve: Médico [Código: 001] Dr(a). Juan Pérez - Especialidad: Cardiología
