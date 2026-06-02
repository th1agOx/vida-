from enum import Enum

class PerfilUsuario(str, Enum):

    SECRETARIA = "secretaria"

    MEDICO = "medico"

    ADMIN = "admin"