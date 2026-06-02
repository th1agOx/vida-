from enum import Enum

class StatusConsulta(str, Enum):
    AGENDADA = "agendada"
    REALIZADA = "realizada"
    CANCELADA = "cancelada"