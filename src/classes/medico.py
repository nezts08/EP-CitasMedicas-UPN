class Medico:
    def __init__(self, codigo: str, nombre: str, especialidad: str):
        self._codigo = codigo
        self._nombre = nombre
        self._especialidad = especialidad

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre  # nos devuelve el nombre del paciente

    @property
    def especialidad(self) -> str:
        return self._especialidad

    def resumen(self) -> str:
        return f"Médico [Código: {self._codigo}] Dr(a). {self._nombre} - Especialidad: {self._especialidad}"
