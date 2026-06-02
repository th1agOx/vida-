class ConsultaRepository:
    def __init__ (self, db):
        self.db = db
### geração de relatorios :
        buscar_por_id()

        listar_agendadas()

        listar_canceladas()

        listar_por_medico()

        listar_por_paciente()
### metodos da regra de negócio :
        existe_agendamento_paciente()

        verificar_horario_disponivel()

        confirmar_consulta()

        cancelar_consulta()