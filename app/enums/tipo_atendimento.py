from enum import Enum

class TipoAtendimento(str, Enum):

    NORMAL = "normal"

    EMERGENCIA = "emergencia"