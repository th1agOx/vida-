from enum import Enum

class TipoExame(str, Enum):
    SANGUINEO = "sanguineo"
    IMAGEM = "imagem"
    OUTRO = "outro"