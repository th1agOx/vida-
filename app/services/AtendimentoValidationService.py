from app.dto.AtendimentoValidationDTO import (
    AtendimentoValidationDTO
)

class AtendimentoValidationService:

    def __init__(
        self,
        paciente_repository,
        consulta_repository,
        pagamento_repository,
        medico_repository
    ):

        self.paciente_repository = paciente_repository

        self.consulta_repository = consulta_repository

        self.pagamento_repository = pagamento_repository

        self.medico_repository = medico_repository
        
    def documentos_validos(
        self,
        paciente_id: int
    ) -> bool:

        paciente = (
            self.paciente_repository
            .buscar_por_id(
                paciente_id
            )
        )

        if paciente is None:
            return False
        
        return (
            paciente.nome is not None
            and 
            paciente.cpf is not None
        )

    def possui_agendamento(
        self,
        paciente_id: int
    ) -> bool:

        return (
            self.consulta_repository
            .possui_agendamento(
                paciente_id
            )
        )

    def pagamento_em_dia(
        self,
        paciente_id : int
    ) -> bool:

        return not (
            self.pagamento_repository
            .possui_pagamento_pendente(
                paciente_id
            )
        )

    def medico_disponivel(
        self,
        consulta_id : int
    ) -> bool:

        return (
            self.medico_repository
            .medico_disponivel(
                consulta_id
            )
        )
    
    def validar(
        self,
        dto: AtendimentoValidationDTO
    ) -> bool:
        
        if dto.tipo_atendimento == "emergencia":

            return self.validar_atendimento_emergencial(
                dto
            )
        return self.vali_atendimento_normal(
            dto
        )   