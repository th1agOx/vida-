from sqlalchemy.orm import Session
from sqlalchemy import Date

from app.models.consulta import Consulta
from app.models.paciente import Paciente
from app.models.medico import Medico

class ConsultaRepository:

    def __init__(self, db: Session):
        self.db = db

    def buscar_consulta_id(
        self,
        consulta_id : int
    ) -> Consulta | None:
        
        return(
            self.db
            .query(Consulta)
            .filter(
                Consulta.id_consulta == consulta_id
            )
            .first()
        )
    
    def listar_por_paciente(
        self,
        paciente_id: int
    ):

        return (
            self.db
            .query(Consulta)
            .filter(
                Consulta.id_paciente == paciente_id
            )
            .all()
        )
    
    def listar_por_medico(
        self,
        medico_id : int,
    ):
        
        return(
            self.db
            .query(Consulta)
            .filter(
                Consulta.id_medico == medico_id
            )
            .all()
        )

    def atualizar(
        self,
        consulta: Consulta
    ) -> Consulta:
        
        self.db.add(
            consulta
        )
        
        self.db.commit()

        self.db.refresh(
            consulta
        )

        return consulta

    def consulta_valida(
        self,
        paciente_id: int
    ) -> bool:

        consulta = (
            self.db
            .query(Consulta)
            .filter(
                Consulta.id_paciente == paciente_id,
                Consulta.status == "agendada"
            )
            .first()
        )
        return consulta is not None