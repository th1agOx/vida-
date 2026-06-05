from sqlalchemy.orm import Session

from app.models.pagamento import Pagamento

class PagamentiRepository:

    def __init__(self, db: Session):
        self.db = db

    def possui_pagamento_pendente(
        self,
        paciente_id: int
    ) -> bool:

        return (
            self.db.query(Pagamento)
            .filter(
                Pagamento.id_paciente == paciente_id,
                Pagamento.status == "PENDENTE"
            )
            .first()
            is not None
    )
    