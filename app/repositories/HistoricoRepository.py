class HistoricoRepository:
    def __init__(self, db):
        self.db = db

        listar_historico_paciente()

        buscar_por_consulta()

        gerar_relatorio_paciente()