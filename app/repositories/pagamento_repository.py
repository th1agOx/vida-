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
                Pagamento.status == "pendente"
            )
            .first()
            is not None
    )

    def criar_cobranca(
        self,
        pagamento: Pagamento
    ) -> Pagamento:

      self.db.add(
          pagamento
      )  

      self.db.commit()

      self.db.refresh(
          pagamento
        )

      return pagamento
    