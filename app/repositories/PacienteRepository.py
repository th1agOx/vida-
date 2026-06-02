import BaseRepository ;

class PacienteRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db)

        buscar_por_id(id)
        buscar_por_cpf(cpf)
        buscar_por_email(email)
        listar_todos()

        contar_pacientes()

        idade_media()

        paciente_mais_novo()

        paciente_mais_velho()
