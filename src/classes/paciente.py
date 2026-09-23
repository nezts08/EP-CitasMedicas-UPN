class Paciente:
    def __init__(self, codigo: str, nombre: str, edad: int):
        if not (0 <= edad <= 120):
            raise ValueError("La edad debe estar entre 0 y 120 años.")
        self._codigo = str(codigo).strip()
        self._nombre = str(nombre).strip()
        self._edad = int(edad)

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def edad(self) -> int:
        return self._edad

    def resumen(self) -> str:
        return f"Paciente [Código: {self._codigo}] {self._nombre} - {self._edad} años"
