import datetime
from pydantic import BaseModel

from app.enums.tipo_atendimento import (
    TipoAtendimento
)

class AtendimentoValidationDTO(BaseModel):

    id_paciente: int

    id_medico: int

    data_hora: datetime

    tipo_atendimento: TipoAtendimento