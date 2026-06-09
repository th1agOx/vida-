from datetime import datetime

from pydantic import BaseModel

class CriarConsultaDTO(BaseModel):

    id_paciente: int

    id_medico: int

    data_hora: datetime

    motivo: str