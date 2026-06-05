from enum import Enum

class TipoPagamento(str, Enum):
    PARTICULAR = "PARTICULAR"
    CONVENIO = "CONVENIO"