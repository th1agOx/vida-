class MedicoRepository:
    def __init__ (self,db):
        self.db = db

        buscar_por_crm()

        buscar_por_especialidade()

        listar_disponiveis()

        esta_disponivel(medico_id,data_hora)