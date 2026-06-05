from app.models.consulta import Consulta

def medico_disponivel(
    self,
    medico_id: int,
    data_hora: datetime
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