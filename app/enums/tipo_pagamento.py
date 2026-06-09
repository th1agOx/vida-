from enum import Enum

class TipoPagamento(str, Enum):
    PARTICULAR = "particular"
    CONVENIO = "convenio"