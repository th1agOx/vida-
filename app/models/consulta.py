from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    ForeignKey,
    DateTime,
    Enum
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.base import Base
from app.enums.status_consulta import StatusConsulta

class Consulta(Base):
    __tablename__ = "consulta"

    id_consulta: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    data_hora: Mapped[datetime] = mapped_column(
        DateTime
    )

    motivo: Mapped[str] = mapped_column(
        String(200)
    )

    status: Mapped[StatusConsulta] = mapped_column(
        Enum(StatusConsulta)
    )

    id_paciente: Mapped[int] = mapped_column(
        ForeignKey("paciente.id_paciente")
    )

    id_medico: Mapped[int] = mapped_column(
        ForeignKey("medico.id_medico")
    )

    paciente = relationship(
        "Paciente",
        back_populates="consultas"
    )

    medico = relationship(
        "Medico",
        back_populates="consultas"
    )

    historico = relationship(
        "HistoricoAtendimento",
        back_populates="consulta",
        uselist=False
    )