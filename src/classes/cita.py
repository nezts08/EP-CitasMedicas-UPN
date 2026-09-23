from .paciente import Paciente
from .medico import Medico


class Cita:
    def __init__(
        self,
        codigo: str,
        paciente: Paciente,
        medico: Medico,
        fecha: str,
        motivo: str = "",
    ):
        self._codigo = str(codigo).strip()
        self._paciente = paciente
        self._medico = medico
        self._fecha = str(fecha).strip()
        self._motivo = str(motivo).strip()
        self._estado = "Programada"
        self._diagnostico = ""

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def paciente(self) -> Paciente:
        return self._paciente

    @property
    def medico(self) -> Medico:
        return self._medico

    @property
    def fecha(self) -> str:
        return self._fecha

    def completar_atencion(self, diagnostico: str):
        self._estado = "Completada"
        self._diagnostico = diagnostico

    def resumen(self) -> str:
        info = (
            f"Cita [{self._codigo}] - Fecha: {self._fecha} | Estado: {self._estado}\n"
            f"  Paciente : {self._paciente.nombre} (Código: {self._paciente.codigo})\n"
            f"  Médico   : Dr(a). {self._medico.nombre} ({self._medico.especialidad})"
        )
        if self._motivo:
            info += f"\n  Motivo   : {self._motivo}"
        if self._diagnostico:
            info += f"\n  Diagnóstico: {self._diagnostico}"
        return info
