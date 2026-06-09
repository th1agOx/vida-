import datetime
from sqlalchemy.orm import Session

from app.models.consulta import Consulta
from app.models.medico import Medico

class MedicoRepository :

    def __init__(self, db: Session):
        self.db = db

    def buscar_medico_id(
        self,
        medico_id : int,
    ) -> Medico | None:
        
        return(
            self.db
            .query(Medico)
            .filter(
                Medico.id_medico == medico_id
            )
            .first()
        )

    def medico_disponivel(
        self,
        medico_id: int,
        data_hora
    ) -> bool:

        consulta = (
            self.db
            .query(Consulta)
            .filter(
                Consulta.id_medico == medico_id,
                Consulta.data_hora == data_hora,
                Consulta.status == "agendada"
            )
            .first()
        )

        return consulta is None