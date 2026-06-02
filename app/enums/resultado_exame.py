from enum import Enum

class ResultadoExame(str, Enum):
    NORMAL = "normal"
    ALTERADO = "alterado"